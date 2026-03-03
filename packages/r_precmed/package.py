# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecmed(RPackage):
	"""Precision Medicine

	A doubly robust precision medicine approach to fit, cross-validate and visualize prediction models for the conditional average treatment effect (CATE). It implements doubly robust estimation and semiparametric modeling approach of treatment-covariate interactions as proposed by Yadlowsky et al. (2020) <doi:10.1080/01621459.2020.1772080>.
	"""
	
	cran = "precmed" 

	version("1.0.0", md5="49fd69ffe1320e36176181295a3141d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
