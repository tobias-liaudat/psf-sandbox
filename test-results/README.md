# Test results

***



## MSE and ellipticity results

- **Dataset**: Simulated data based on the CFIS ellipticity variations using Sextractor

This test provide a fair comparison between the RCA-family methods and the original PSFEx on simulated data.

Tests 22 to 28 are done over the Sextractor dataset so PSFEx can be used as comparison and the pixel-MSE values are calculated.

|      Tests                         |  pixel-MSE     | pixel-RMSE     |  e1-RMSE   | e2-RMSE    |  R2-RMSE   |
|:----------------------------------:|:--------------:|:--------------:|:----------:|:----------:|:----------:|
|**22**: RCA_PSFEx (KSIG=0.1)        |  2.365074e-07  |  4.863203e-04  |  0.001061  |  0.000680  |  0.486363  |
|**23**: RCA_hybrid (eig18, KSIG=0.1)|  4.419285e-07  |  6.647770e-04  |**0.000851**|  0.000694  |  0.307546  |
|**24**: RCA (eig24, KSIG=0.1)       |  4.597328e-07  |  6.780360e-04  |  0.000906  |**0.000670**|**0.300346**|
|**25**: RCA_PSFEx (KSIG=0)          |  2.476524e-07  |  4.976468e-04  |  0.001030  |  0.000680  |  0.486895  |
|**26**: RCA_PSFEx (KSIG=1)          |**2.003553e-07**|**4.476107e-04**|  0.001540  |  0.000689  |  0.460138  |
|**27**: RCA_PSFEx (KSIG=3)          |  2.015617e-07  |  4.489562e-04  |  0.002516  |  0.000777  |  0.399802  |
|**28**: PSFEx                       |  4.112598e-07  |  6.412954e-04  |  0.001019  |  0.000693  |  0.399379  |


## Test descriptions

<table>
<tr><th> Test 22 </th><th> Test 23 </th><th> Test 24 </th></tr>
<tr><td>

|      Test 22  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    6  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.1    |
| Apply_degrad |  True  |
|   ALPHA      |   PSFEx |

</td><td>

|     Test 23   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    18  |
|  n_eigenVec  |    5  |
|  sigmaNoise  | 1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.1    |
| Apply_degrad |  True  |
|   ALPHA      |   hybrid_1 |

</td><td>

|   Test 24     |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5  |
|  sigmaNoise  | 1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.1    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td></tr> </table>


<table>
<tr><th> Test 25 </th><th> Test 26 </th><th> Test 27 </th></tr>
<tr><td>

|    Test 25    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    6  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.0    |
| Apply_degrad |  True  |
|   ALPHA      |   PSFEx |


</td><td>

|   Test 26     |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    6  |
|  n_eigenVec  |    5  |
|  sigmaNoise  | 1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   1.0    |
| Apply_degrad |  True  |
|   ALPHA      |   PSFEx |

</td><td>

|     Test 27   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    6  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   3.0    |
| Apply_degrad |  True  |
|   ALPHA      |   PSFEx |

</td></tr> </table>


<table>
<tr><th> Test 28 </th></tr>
<tr><td>

|      Test 28  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  PSFEx  |    regular parameters  |
|  sigmaNoise  | 1e-3 |
|   test_per   |   0.5  |

</td></tr> </table>


## Test plots

### Test 22

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test22.png" width="800" align="middle">

### Test 23

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test23.png" width="800" align="middle">

### Test 24

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test24.png" width="800" align="middle">

### Test 25

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test25.png" width="800" align="middle">

### Test 26

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test26.png" width="800" align="middle">

### Test 27

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test27.png" width="800" align="middle">

### Test 28

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test28.png" width="800" align="middle">


***

# TL

## Test summary

### Simulated data

<table>
<tr><th> Test 1 </th><th> Test 2 </th><th> Test 3 </th></tr>
<tr><td>

|      Test 1  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|     Test 2   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|   Test 3     |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    20  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td></tr> </table>


<table>
<tr><th> Test 4 </th><th> Test 5 </th><th> Test 7 </th><th> Test 8 </th></tr>
<tr><td>

|    Test 4    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    8   |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |


</td><td>

|   Test 5     |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    4   |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|     Test 7   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    50  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|     Test 8   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    50  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td></tr> </table>

<table>
<tr><th> Test 9 </th><th> Test 10 </th><th> Test 11 </th></tr>
<tr><td>

|      Test 9  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|     Test 10  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.5  |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|   Test 11    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td></tr> </table>

<table>
<tr><th> Test 14 </th><th> Test 15 </th><th> Test 16 </th><th> Test 17 </th></tr>
<tr><td>

|    Test 14   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      |   None |



</td><td>

|   Test 15    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |    
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |   1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      | PSFEx  |

</td><td>

|     Test 16  |  Value |
|:------------:|:------:|
|  CCD_n       |    2   |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|     Test 17  |  Value |
|:------------:|:------:|
|  CCD_n       |    2   |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      |  PSFEx |

</td></tr> </table>

### Hybrid Tests

<table>
<tr><th> Test 18 </th><th> Test 19 </th></tr>
<tr><td>

|      Test 18 |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    18  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
|   nb_iter    |   3    |
| Apply_degrad |  True  |
|   ALPHA      | hybrid_1 |

</td><td>

|     Test 19  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    18  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
|   nb_iter    |   3    |
| Apply_degrad |  True  |
|   ALPHA      | hybrid_2 |

</td></tr> </table>

### Reuced simulated data (data subset)

<table>
<tr><th> Test 12 </th><th> Test 13 </th></tr>
<tr><td>

|      Test 12 |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
|   nb_iter    |   4    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td><td>

|     Test 13  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
|   nb_iter    |   2    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

</td></tr> </table>

### Real CFIS data

#### Test and train on _the same_ star catalog, CCD = 38

<table>
<tr><th> Test 1 </th><th> Test 2 </th><th> Test 3 </th><th> Test 4 </th></tr>
<tr><td>

|      Test 1  |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    8   |
|  n_eigenVec  |    10  |
|   test_per   |   1    |
|   KSIG       |   3    |
| Apply_degrad |  True  |

</td><td>

|     Test 2   |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    10  |
|   test_per   |   1    |
|   KSIG       |   3    |
| Apply_degrad |  True  |

</td><td>

|   Test 3     |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    10  |
|   test_per   |   1    |
|   KSIG       |   3    |
| Apply_degrad |  True  |

</td><td>

|   Test 4     |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|   test_per   |   1    |
|   KSIG       |   0.5  |
| Apply_degrad |  True  |

</td></tr> </table>



#### Test and train on _separate_ star catalogs, CCD = 38

<table>
<tr><th> Test 5 </th><th> Test 6 </th></tr>
<tr><td>

|      Test 5  |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|   test_per   |   1    |
|   KSIG       |   0.5  |
| Apply_degrad |  True  |

</td><td>

|     Test 6   |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|   test_per   |   1    |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |

</td></tr> </table>




***

## Test 1

|     Test 1   |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test1.png" width="800" align="middle">

## Test 2

|     Test 2   |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test2.png" width="800" align="middle">

## Test 3

|    Test 3    |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    20  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test3.png" width="800" align="middle">

## Test 4

|   Test 4     |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    8   |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test4.png" width="800" align="middle">

## Test 5

|   Test 5     |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    4   |
|  n_eigenVec  |    10  |
|  sigmaNoise  | 0.4e-3 |
|   test_per   |   0.8  |
|   KSIG       |   3    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test5.png" width="800" align="middle">



## Test 7

- JB dataset: Consists of simulated stars. Each catalog (of one CCD) includes 50 test stars, one for each pixel and is placed on each one of their centres. Then 50 train stars that maintain the ellipticity of their corresponding pixel but are shifted within the domains of its pixel. The pixels of the train stars are picked randomly so there might be pixels with more than one star and pixels with no stars at all.

|      Test 7  |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    50  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/test-7-3D.png" width="600" align="middle">

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test7.png" width="800" align="middle">


## Test 8

- JB datase used.

|     Test 8   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    50  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   None |


<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/test-8-3D.png" width="600" align="middle">

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test8.png" width="800" align="middle">



## Test 9

|      Test 9  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test9.png" width="800" align="middle">

## Test 10

|     Test 10  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    32  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.5  |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test10.png" width="800" align="middle">

## Test 11

|   Test 11    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test11.png" width="800" align="middle">

## Test 12

| Reduced dataset |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
|   nb_iter    |   4    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test12.png" width="800" align="middle">

## Test 13

| Reduced dataset |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    16  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   1    |
|   nb_iter    |   2    |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test13.png" width="800" align="middle">

## Test 14

|    Test 14   |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test14.png" width="800" align="middle">

## Test 15

|   Test 15    |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |    
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |   1e-3 |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      | PSFEx  |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test15.png" width="800" align="middle">

## Test 16

|     Test 16  |  Value |
|:------------:|:------:|
|  CCD_n       |    2   |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      |   None |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test16.png" width="800" align="middle">

## Test 17

|     Test 17  |  Value |
|:------------:|:------:|
|  CCD_n       |    2   |
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|  sigmaNoise  |  1e-3  |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
| Apply_degrad |  True  |
|   ALPHA      |  PSFEx |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test17.png" width="800" align="middle">


## Test 18

|      Test 18 |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    18  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
|   nb_iter    |   3    |
| Apply_degrad |  True  |
|   ALPHA      | hybrid_1 |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test18.png" width="800" align="middle">


## Test 19

|     Test 19  |  Value |
|:------------:|:------:|
|  CCD_n       |    38  |
|  n_eigenPSF  |    18  |
|  n_eigenVec  |    5   |
|  sigmaNoise  | 1e-3   |
|   test_per   |   0.5  |
|   KSIG       |   0.1  |
|   nb_iter    |   3    |
| Apply_degrad |  True  |
|   ALPHA      | hybrid_2 |

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/test-results/imgs/TL_test19.png" width="800" align="middle">


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
