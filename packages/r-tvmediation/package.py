# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvmediation(RPackage):
	"""Time Varying Mediation Analysis

	Provides functions for estimating mediation effects that vary over 
   time as described in Cai X, Coffman DL, Piper ME, Li R. 
   Estimation and inference for the mediation effect in a time-varying mediation model. 
   BMC Med Res Methodol. 2022;22(1):1-12.
	"""
	
	homepage = "https://github.com/dcoffman/tvmediation/wiki"
	cran = "tvmediation" 

	version("1.1.0", md5="cbbb626e7c4d6947a1d1d057fd79b622")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-locpol@0.7.0:", type=("build", "run"))
