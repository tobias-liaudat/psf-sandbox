# Detailed Analysis of test 14

## Test characteristics

- Using catalog n1 to plot the results, except for the ellipticity residual that uses all the catalogs.

|    Test 14   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
|   nb_iter    |   2    |
| Apply_degrad |  True  |
|   ALPHA      |   None |


## Ellipticity residual map

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/TL_test14.png" width="600" align="middle">

## Model's final matrix

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/A_VT_alpha_test14-cat_1.png" width="600" align="middle">

## EigenPSF energy distribution

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/test_14-cat_1.png" width="600" align="middle">

## EigenPSF contribution GIF (ordered by energy)

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/superGIF_test14.gif" width="600" align="middle">

## EigenPSF contribution GIF (ordered by proximity metric)

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/proxMetric_superGIF_test14.gif" width="600" align="middle">

## PSF model images

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/test-14-PSF-0000001-38.png" width="600" align="middle">


## Residual model images

- Test stars are noiseless while the train stars are noisy.

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/test-14-res-0000001-38.png" width="600" align="middle">


## Test star model images

- Test stars are noiseless while the train stars are noisy.

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-14/imgs/test-14-testStars-0000001-38.png" width="600" align="middle">
