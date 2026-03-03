# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginSurvival(RPackage):
	"""R Commander Plug-in for the 'survival' Package

	An R Commander plug-in for the survival
  package, with dialogs for Cox models, parametric survival regression models,
  estimation of survival curves, and testing for differences in survival
  curves, along with data-management facilities and a variety of tests, 
  diagnostics and graphs.
	"""
	
	cran = "RcmdrPlugin.survival" 

	version("1.3-2", md5="5b0f73f7691c26a4abc0e25ccf5a1882")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-date", type=("build", "run"))
	depends_on("r-rcmdr@2.8.0:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
