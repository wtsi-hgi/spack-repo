# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwexp(RPackage):
	"""Piecewise Exponential Distribution Prediction Model

	Build piecewise exponential survival model for study design (planning) and event/timeline prediction. 
	"""
	
	homepage = "https://github.com/zjph602xtc/PWEXP"
	cran = "PWEXP" 

	version("0.4.4", md5="0f84d6a11588495a6401dd38ca8755b3")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
