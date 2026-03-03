# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockforest(RPackage):
	"""Block Forests: Random Forests for Blocks of Clinical and Omics
Covariate Data

	A random forest variant 'block forest' ('BlockForest') tailored to the 
  prediction of binary, survival and continuous outcomes using block-structured 
  covariate data, for example, clinical covariates plus measurements of a certain 
  omics data type or multi-omics data, that is, data for which measurements of 
  different types of omics data and/or clinical data for each patient exist. Examples 
  of different omics data types include gene expression measurements, mutation data
  and copy number variation measurements.
  Block forest are presented in Hornung & Wright (2019). The package includes four
  other random forest variants for multi-omics data: 'RandomBlock', 'BlockVarSel', 
  'VarProb', and 'SplitWeights'. These were also considered in Hornung & Wright (2019), 
  but performed worse than block forest in their comparison study based on 20 real 
  multi-omics data sets. Therefore, we recommend to use block forest ('BlockForest') 
  in applications. The other random forest variants can, however, be consulted for 
  academic purposes, for example, in the context of further methodological 
  developments. 
  Reference: Hornung, R. & Wright, M. N. (2019) Block Forests: random forests for blocks of clinical and omics covariate data. BMC Bioinformatics 20:358. <doi:10.1186/s12859-019-2942-y>.
	"""
	
	homepage = "https://github.com/bips-hb/blockForest"
	cran = "blockForest" 

	version("0.2.6", md5="cd53457e6aa9d802ecef243e95f753dc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
