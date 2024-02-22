# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurvir(RPackage):
	"""Specify Reserve Demand Curves

	Automatic specification and estimation of reserve demand curves for central bank operations. The package can help to choose the best demand curve and identify additional explanatory variables. Various plot and predict options are included. For more details, see Chen et al. (2023) <https://www.imf.org/en/Publications/WP/Issues/2023/09/01/Modeling-the-Reserve-Demand-to-Facilitate-Central-Bank-Operations-538754>. 
	"""
	
	cran = "curvir" 

	version("0.1.1", md5="f0ab6b001e89c4655565a895c9d3e8ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-qgam", type=("build", "run"))
	depends_on("r-quantregforest", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
