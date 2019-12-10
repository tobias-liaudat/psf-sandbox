# Test results

***

# JB

## Test 1

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    4   |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.8  |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/JB_test1.png" width="600" align="middle">

## Test 2

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    8   |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.8  |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/JB_test2.png" width="600" align="middle">

## Test 3

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |   16   |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.8  |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/JB_test3.png" width="600" align="middle">

## Test 4

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |   32   |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.8  |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/JB_test4.png" width="600" align="middle">

***

# TL

## Test 1

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/2d-plot-test1.png" width="600" align="middle">

## Test 2

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/2d-plot-test2.png" width="600" align="middle">

## Test 3

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    20  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/2d-plot-test3.png" width="600" align="middle">

## Test 4

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    8   |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/2d-plot-test4.png" width="600" align="middle">

## Test 5

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    4   |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/2d-plot-test5.png" width="600" align="middle">



## Test 7

- JB dataset: Consists of simulated stars. Each catalog (of one CCD) includes 50 test stars, one for each pixel and is placed on each one of their centres. Then 50 train stars that maintain the ellipticity of their corresponding pixel but are shifted within the domains of its pixel. The pixels of the train stars are picked randomly so there might be pixels with more than one star and pixels with no stars at all.

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    50  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/test-7-3D.png" width="600" align="middle">

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test7.png" width="600" align="middle">


## Test 8

- JB datase used.

|              |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    50  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/test-8-3D.png" width="600" align="middle">

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test8.png" width="600" align="middle">
