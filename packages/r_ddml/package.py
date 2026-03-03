# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdml(RPackage):
	"""Double/Debiased Machine Learning

	Estimate common causal parameters using double/debiased machine 
    learning as proposed by Chernozhukov et al. (2018) <doi:10.1111/ectj.12097>. 
    'ddml' simplifies estimation based on (short-)stacking as discussed in 
    Ahrens et al. (2024) <arXiv:2401.01645>, which leverages multiple base 
    learners to increase robustness to the underlying data generating process.
	"""
	
	homepage = "https://github.com/thomaswiemann/ddml"
	cran = "ddml" 

	version("0.2.0", md5="763b776cee6e701ec10e361ba84bfe2a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
