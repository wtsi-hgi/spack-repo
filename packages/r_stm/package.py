# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStm(RPackage):
	"""Estimation of the Structural Topic Model

	The Structural Topic Model (STM) allows researchers 
  to estimate topic models with document-level covariates. 
  The package also includes tools for model selection, visualization,
  and estimation of topic-covariate regressions. Methods developed in
  Roberts et. al. (2014) <doi:10.1111/ajps.12103> and 
  Roberts et. al. (2016) <doi:10.1080/01621459.2016.1141684>. Vignette
  is Roberts et. al. (2019) <doi:10.18637/jss.v091.i02>.
	"""
	
	homepage = "http://www.structuraltopicmodel.com/"
	cran = "stm" 

	version("1.3.7", md5="4c357c7e82ce5d8b6ed1f4b85142f31a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
