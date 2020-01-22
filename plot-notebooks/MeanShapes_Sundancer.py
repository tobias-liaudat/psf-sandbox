import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits
import sys

# MegaCam -> plt.subplot correspondance, as given by:
'''        'COMMENT Unique detector IDs for MegaCam (North on top, East to the left)',
           'COMMENT    --------------------------',
           'COMMENT    ba ba ba ba ba ba ba ba ba',
           'COMMENT    00 01 02 03 04 05 06 07 08',
           'COMMENT --------------------------------',
           'COMMENT ba ba ba ba ba ba ba ba ba ba ba',
           'COMMENT 36 09 10 11 12 13 14 15 16 17 37',
           'COMMENT --------------------------------',
           'COMMENT 38 18 19 20 21 22 23 24 25 26 39',
           'COMMENT ab ab ab ab ab ab ab ab ab ab ab',
           'COMMENT --------------------------------',
           'COMMENT    27 28 29 30 31 32 33 34 35',
           'COMMENT    ab ab ab ab ab ab ab ab ab',
           'COMMENT    __________________________'
'''
def MegaCamPos(j):
    if j < 9:
        # first row - shift by one
        return j+1
    elif j < 18:
        # second row, non-ears
        return j+3
    elif j < 27:
        # third row non-ears
        return j+5
    elif j < 36:
        # fourth row
        return j+7
    else:
        MegaCamCoords = {36:11, 37:21, 38:22, 39:32}
        return MegaCamCoords[j]

def MegaCamFlip(xbins, ybins, ccd_nb, nb_pixel):
    if ccd_nb < 18 or ccd_nb in [36,37]:
        # swap x axis so origin is on top-right
        xbins = nb_pixel[0] - xbins + 1
    else:
        # swap y axis so origin is on bottom-left
        ybins = nb_pixel[1] - ybins + 1
    return xbins, ybins

def MeanShapesPlot(ccd_maps, filename, title='', colorbar_ampl=1., wind=None, cmap='bwr'):
    # colorbar amplitude
    if wind is None:
        vmax = max(np.nanmax(ccd_maps), np.abs(np.nanmin(ccd_maps))) * colorbar_ampl
        vmin = -vmax * colorbar_ampl
    else:
        vmin, vmax = wind[0]*colorbar_ampl, wind[1]*colorbar_ampl

    # create full plot
    fig, axes = plt.subplots(nrows=4,ncols=11)
    # remove corner axes (above and below ears)
    for j in [0, 10, -1, -11]:
        axes.flat[j].axis('off')
    for ccd_nb,ccd_map in enumerate(ccd_maps):
        ax = axes.flat[MegaCamPos(ccd_nb)]
        im = ax.imshow(ccd_map.T,cmap=cmap,interpolation='Nearest',vmin=vmin,vmax=vmax)
        ax.set_xticks([])
        ax.set_yticks([])
    plt.suptitle(title) #TODO: fix title
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)
    plt.savefig('{}.png'.format(filename))
    plt.close()

def main():
    """ Compute and plot average shapes (e1, e2, R^2) on both stars and PSF model, and
    plot them on the MegaCam mosaic. Syntax:

    > python MeanShapes.py gridsize_x gridsize_y path/to/starcat
    Where gridsize_x and gridsize_y determine the number of bins per CCD in the horizontal
    and vertical directions, and path/to/starcat is the path to the full validation star
    catalog. colorbar_ampl is the (optional) multiplier to be applied for the residual plot.
    Can also be set to 'auto' to just use its amplitude.pyt
    """
    nb_pixel = int(sys.argv[1]),int(sys.argv[2])
    starcat_path = sys.argv[3]
    if len(sys.argv) > 4:
        if sys.argv[4] != 'auto':
            auto_colorbar = False
            colorbar_ampl = 1./float(sys.argv[4])
        else:
            auto_colorbar = True
            colorbar_ampl = 1.
    else:
        auto_colorbar = False
        colorbar_ampl = 1.
    # MegaCam: each CCD is 2048x4612
    grid = np.linspace(0, 2048, nb_pixel[0]+1), np.linspace(0, 4612, nb_pixel[1]+1)

    # READ FULL STARCAT
    starcat = fits.open(starcat_path)[2].data

    # Flag mask
    star_flags = starcat['FLAG_STAR_HSM']
    psf_flags = starcat['FLAG_PSF_HSM']
    flagmask = np.abs(star_flags-1) * np.abs(psf_flags-1)

    # convert sigma to R^2's
    all_star_shapes = np.array([starcat['E1_STAR_HSM'],starcat['E2_STAR_HSM'],
                            2.*starcat['SIGMA_STAR_HSM']**2])
    all_psf_shapes = np.array([starcat['E1_PSF_HSM'],starcat['E2_PSF_HSM'],
                            2.*starcat['SIGMA_PSF_HSM']**2])

    print('TOTAL e1 residual RMSE: %.6f\n'%(np.sqrt(np.mean((all_star_shapes[0,:] - all_psf_shapes[0,:])**2))))
    print('TOTAL e2 residual RMSE: %.6f\n'%(np.sqrt(np.mean((all_star_shapes[1,:] - all_psf_shapes[1,:])**2))))
    print('TOTAL R2 residual RMSE: %.6f\n'%(np.sqrt(np.mean((all_star_shapes[2,:] - all_psf_shapes[2,:])**2))))

    ccd_maps = np.ones((40, 2, 4)+nb_pixel) * np.nan # CCDs x star/model x (e1,e2,R2,nstars) x xpos x ypos
    for ccd_nb,ccd_map in enumerate(ccd_maps):
        # handle different scatalog versions
        try:
            ccd_mask = ((starcat['CCD_NB']==ccd_nb) * flagmask).astype(bool)
        except TypeError:
            ccd_mask = ((starcat['CCD_NB']==str(ccd_nb)) * flagmask).astype(bool)

        star_shapes = all_star_shapes[:,ccd_mask]
        psf_shapes = all_psf_shapes[:,ccd_mask]

        xs, ys = starcat['X'][ccd_mask], starcat['Y'][ccd_mask]
        xbins = np.digitize(xs, grid[0])
        ybins = np.digitize(ys, grid[1])
        # swap axes to match CCD orientation and origin convention
        xbins, ybins = MegaCamFlip(xbins, ybins, ccd_nb, nb_pixel)
        for xb in range(nb_pixel[0]):
            for yb in range(nb_pixel[1]):
                bin_star_shapes = star_shapes[:,(xbins==xb+1) * (ybins==yb+1)]
                bin_psf_shapes = psf_shapes[:,(xbins==xb+1) * (ybins==yb+1)]
                ccd_map[0,:3,xb,yb] = np.mean(bin_star_shapes,axis=1)
                ccd_map[1,:3,xb,yb] = np.mean(bin_psf_shapes,axis=1)
                ccd_map[:,3,xb,yb] = bin_star_shapes.shape[1]

    # e_1
    vmax = max(np.nanmax(ccd_maps[:,:,0]), np.abs(np.nanmin(ccd_maps[:,:,0])))
    vmin = -vmax
    wind = [vmin, vmax]
    MeanShapesPlot(ccd_maps[:,0,0], 'e1s', r'$e_1$ (stars)', wind=wind)
    MeanShapesPlot(ccd_maps[:,1,0], 'e1m', r'$e_1$ (model)', wind=wind)
    if auto_colorbar:
        wind=None
    MeanShapesPlot(ccd_maps[:,0,0]-ccd_maps[:,1,0], 'e1res', r'$e_1$ residual', wind=wind,
            colorbar_ampl=colorbar_ampl)
    e1_res = ccd_maps[:,0,0]-ccd_maps[:,1,0]
    e1_res = e1_res[~np.isnan(e1_res)]
    print('e1 residual RMSE: %.6f\n'%(np.sqrt(np.mean((e1_res)**2))))

    # e_2
    vmax = max(np.nanmax(ccd_maps[:,:,1]), np.abs(np.nanmin(ccd_maps[:,:,0])))
    vmin = -vmax
    wind = [vmin, vmax]
    MeanShapesPlot(ccd_maps[:,0,1], 'e2s', r'$e_2$ (stars)', wind=wind)
    MeanShapesPlot(ccd_maps[:,1,1], 'e2m', r'$e_2$ (model)', wind=wind)
    if auto_colorbar:
        wind=None
        colorbar_ampl = 1.
    MeanShapesPlot(ccd_maps[:,0,1]-ccd_maps[:,1,1], 'e2res', r'$e_2$ residual', wind=wind,
            colorbar_ampl=colorbar_ampl)
    e2_res = ccd_maps[:,0,1]-ccd_maps[:,1,1]
    e2_res = e2_res[~np.isnan(e2_res)]
    print('e2 residual RMSE: %.6f\n'%(np.sqrt(np.mean((e2_res)**2))))

    # R^2
    wind = [0,np.nanmax(ccd_maps[:,:,2])]
    colorbar_ampl = 1
    MeanShapesPlot(ccd_maps[:,0,2], 'R2s', r'$R^2$ (stars)', wind=wind, cmap='Reds')
    MeanShapesPlot(ccd_maps[:,1,2], 'R2m', r'$R^2$ (model)', wind=wind, cmap='Reds')
    if auto_colorbar:
        wind=[0,np.nanmax(np.abs(ccd_maps[:,0,2]-ccd_maps[:,1,2]))]
        colorbar_ampl = 1.
    MeanShapesPlot(np.abs(ccd_maps[:,0,2]-ccd_maps[:,1,2]), 'R2res', r'$R^2$ absolute residual', wind=wind,
            colorbar_ampl=colorbar_ampl, cmap='Reds')
    R2_res = ccd_maps[:,0,2]-ccd_maps[:,1,2]
    R2_res = R2_res[~np.isnan(R2_res)]
    print('R2 residual RMSE: %.6f\n'%(np.sqrt(np.mean((R2_res)**2))))

    # nstars
    wind=(0,np.max(ccd_maps[:,0,3]))
    MeanShapesPlot(ccd_maps[:,0,3], 'nstar', r'Number of stars', wind=wind, cmap='magma')


if __name__ == "__main__":
    main()
