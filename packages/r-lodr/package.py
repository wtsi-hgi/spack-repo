# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLodr(RPackage):
	"""Linear Model Fitting with LOD Covariates

	Tools to fit linear regression model to data while taking into account covariates with lower limit of detection (LOD).
	"""
	
	cran = "lodr" 

	version("1.0", md5="1f701424aaa3f1c0c21179795992b8cb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
