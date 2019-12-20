# Detailed Analysis of test 15

## Test characteristics

- Using catalog n1 to plot the results, except for the ellipticity residual that uses all the catalogs.

|   Test 15    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |    
|  n_eigenPSF  |    6   |
|  n_eigenVec  |    5   |
|  sigmaNoise  |   1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      | PSFEx  |


## Ellipticity residual map

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/TL_test15.png" width="600" align="middle">

## Model's final matrices

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/A_VT_alpha_test15-cat_1.png" width="1500" align="middle">

## EigenPSF energy distribution

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/test_15-cat_1.png" width="800" align="middle">

## EigenPSF contribution GIF (ordered by energy)

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/superGIF_test15.gif" width="800" align="middle">

## EigenPSF contribution GIF (ordered by proximity metric)

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/proxMetric_superGIF_test15.gif" width="800" align="middle">

## PSF model images

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/test-15-PSF-0000001-38.png" width="1000" align="middle">


## Residual model images

- Test stars are noiseless while the train stars are noisy.

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/test-15-res-0000001-38.png" width="1000" align="middle">


## Test star model images

- Test stars are noiseless while the train stars are noisy.

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/detailed-analysis/test-15/imgs/test-15-testStars-0000001-38.png" width="1000" align="middle">
