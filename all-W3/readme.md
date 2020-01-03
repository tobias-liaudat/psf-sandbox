# Test over all W3 from CFIS

- The test where done using real data from CFIS.

- For the complete set of result images go to the imgs folder.

- The training and the validation was done over the same set of stars (all of them).

***

### Test's parameters

<table>
<tr><th> RCA_4 </th><th> RCA_24 </th><th> RCA_Hybrid </th><th> RCA_PSFEx </th><th> PSFEx </th></tr>
<tr><td>

|    RCA_4     |  Value  |
|:------------:|:------:|
|  n_eigenPSF  |    4   |
|  n_eigenVec  |    5   |
|   KSIG       |   3    |
|   nb_iter    |   2    |
| Apply_degrad |  True  |
|   ALPHA      |   None |


</td><td>

|    RCA_24    |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    24  |
|  n_eigenVec  |    5   |
|   KSIG       |   0.1  |
|   nb_iter    |   2    |
| Apply_degrad |  True  |
|   ALPHA      |   None |


</td><td>

|  RCA_Hybrid  |  Value |
|:------------:|:------:|
|  n_eigenPSF  |   18 (+6)  |
|  n_eigenVec  |   5  |
|   KSIG       |   0.1    |
|   nb_iter    |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   hybrid_1 |

</td><td>

|    RCA_PSFEx   |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    6  |
|  n_eigenVec  |    5   |
|   KSIG       |   0.1    |
|   nb_iter    |   3    |
| Apply_degrad |  True  |
|   ALPHA      |   PSFEx |

</td><td>

|     PSFEx   |  Value |
|:------------:|:------:|
|  n_eigenPSF  |    6  |
|  Standard config  |    True  |


</td></tr> </table>


### Test RMSE performance

The RMSE calculated on all the test/train stars before any mean is performed.

| Residues RMSE |  RCA_4    |  RCA_24   |  RCA_Hybrid |  RCA_PSFEx |  PSFEx        |
|:-------------:|:---------:|:---------:|:-----------:|:----------:|:-------------:|
|  e1           | 0.018127  | 0.017439  | 0.016467    | 0.016626   | **0.016449**  |
|  e2           | 0.017123  | 0.016727  | **0.016203** | 0.016486  | 0.016313  |
|  R2           | 4.795213  | 5.260821  | 3.989269    | 2.873945   | **2.873515**  |


The RMSE of the residues was calculated on a CCD segmented on a 5x10 grid where the different values where the mean of the values on the bin is considered.

| Residues RMSE 5x10 grid |  RCA_4    |  RCA_24   |  RCA_Hybrid |  RCA_PSFEx |  PSFEx        |
|:-------------:|:---------:|:---------:|:-----------:|:----------:|:-------------:|
|  e1           | 0.005348  | 0.002530  | 0.001494    | 0.001373   | **0.001235**  |
|  e2           | 0.003055  | 0.001660  | 0.001313    | 0.001356   | **0.001263**  |
|  R2           | 0.470739  | 0.88649   |  0.439035   | 0.319939   | **0.317929**  |


## CCD Cam plots: *e1 residue*

### RCA_4

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/RCA-4/e1res.png" width="600" align="middle">

### RCA_24

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/RCA-24/e1res.png" width="600" align="middle">

### RCA_Hybrid

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_RCA_hybrid/5_10/e1res.png" width="600" align="middle">

### RCA_PSFEx

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_RCA_PSEFEx/5_10/e1res.png" width="600" align="middle">

### PSFEx

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_PSFEx/5_10/e1res.png" width="600" align="middle">


***


## CCD Cam plots: *e2 residue*

### RCA_4

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/RCA-4/e2res.png" width="600" align="middle">

### RCA_24

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/RCA-24/e2res.png" width="600" align="middle">

### RCA_Hybrid

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_RCA_hybrid/5_10/e2res.png" width="600" align="middle">

### RCA_PSFEx

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_RCA_PSEFEx/5_10/e2res.png" width="600" align="middle">

### PSFEx

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_PSFEx/5_10/e2res.png" width="600" align="middle">


***


## CCD Cam plots: *R2 residue*

### RCA_4

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/RCA-4/R2res.png" width="600" align="middle">

### RCA_24

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/RCA-24/R2res.png" width="600" align="middle">

### RCA_Hybrid

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_RCA_hybrid/5_10/R2res.png" width="600" align="middle">

### RCA_PSFEx

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_RCA_PSEFEx/5_10/R2res.png" width="600" align="middle">

### PSFEx

<img src="https://github.com/tobias-liaudat/psf-sandbox/blob/master/all-W3/imgs/test_W3_PSFEx/5_10/R2res.png" width="600" align="middle">
