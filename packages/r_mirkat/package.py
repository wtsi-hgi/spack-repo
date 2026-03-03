# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirkat(RPackage):
	"""Microbiome Regression-Based Kernel Association Tests

	Test for overall association between microbiome composition data 
  and phenotypes via phylogenetic kernels. The phenotype can be univariate 
  continuous or binary (Zhao et al. (2015) <doi:10.1016/j.ajhg.2015.04.003>), 
  survival outcomes (Plantinga et al. (2017) <doi:10.1186/s40168-017-0239-9>), 
  multivariate (Zhan et al. (2017) <doi:10.1002/gepi.22030>) and 
  structured phenotypes (Zhan et al. (2017) <doi:10.1111/biom.12684>). 
  The package can also use robust regression (unpublished work) and 
  integrated quantile regression (Wang et al. (2021) <doi:10.1093/bioinformatics/btab668>). 
  In each case, the microbiome community effect is modeled nonparametrically 
  through a kernel function, which can incorporate phylogenetic tree information. 
	"""
	
	cran = "MiRKAT" 

	version("1.2.3", md5="03b7cd229fa078187f418b0325b21df2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-gunifrac", type=("build", "run"))
	depends_on("r-pearsonds", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
