# RAS

## Overview
This code is used for re-balancing or disaggregating an n by m matrix using the RAS algorithm. The application of this algorithm is to fill n unknown elements in an Input Output Table, either for projected results, or when splitting economic sectors. This algorithm uses a 'seed' matrix as the basis for bi-proportional re-balancing of a 'goal' matrix, using a new set of row and column sums. The intention is to produce a new matrix which has otherwise unknown matrix elements, using known row and column sums and known matrix elements for a similarly proportioned matrix.

The algorithm is complete when there are no differences between the row and column totals (i.e. when the matrix is balanced). 


## Requirements
The algorithm was written using the following packages;
* numpy==1.14.2
* pandas==0.25.2

There are no other known dependencies.


## References
RAS Algorithm based on;
* Lui, Lenzen & Murray (2012) doi: [10.1111/j.1477-8947.2012.01439.x](https://doi.org/10.1111/j.1477-8947.2012.01439.x)

* Wiedmann et al. (2011) doi: [10.1021/es2007287](https://doi.org/10.1021/es2007287)

## Open Access and transparency

This code is provided open access in accordance with NERC [Guidance on Preservation of NERC Model Code and Model Output](https://nerc.ukri.org/research/sites/data/policy/modelcode-guidance/)



