# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetzrcr(RPackage):
	"""Compare Detrital Zircon Suites

	Compare detrital zircon suites by uploading univariate,
      U-Pb age, or bivariate, U-Pb age and Lu-Hf data, in a 'shiny'-based
      user-interface. Outputs publication quality figures using 'ggplot2', and
      tables of statistics currently in use in the detrital zircon geochronology
      community.
	"""
	
	homepage = "https://github.com/magnuskristoffersen/detzrcr"
	cran = "detzrcr" 

	version("0.3.1", md5="14db0ab35b182e822a8cfa73dcee4a41")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
