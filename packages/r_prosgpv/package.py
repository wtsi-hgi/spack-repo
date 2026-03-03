# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProsgpv(RPackage):
	"""Penalized Regression with Second-Generation P-Values

	Implementation of penalized regression with second-generation p-values for variable
    selection. The algorithm can handle linear regression, GLM, and Cox regression. S3 methods print(), summary(), coef(), predict(), and plot() are available for the algorithm. Technical details
    can be found at Zuo et al. (2021) <doi:10.1080/00031305.2021.1946150>. 
	"""
	
	homepage = "https://github.com/zuoyi93/ProSGPV"
	cran = "ProSGPV" 

	version("1.0.0", md5="940f6ed4c2ef6ea14f354c8ed302221b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-brglm2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
