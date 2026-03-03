# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFableProphet(RPackage):
	"""Prophet Modelling Interface for 'fable'

	Allows prophet models from the 'prophet' package to be used in a tidy workflow with the modelling interface of 'fabletools'. This extends 'prophet' to provide enhanced model specification and management, performance evaluation methods, and model combination tools.
	"""
	
	homepage = "https://pkg.mitchelloharawild.com/fable.prophet/"
	cran = "fable.prophet" 

	version("0.1.0", md5="61b4de704f0e9a251a86425314306eb7")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fabletools@0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-prophet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-distributional", type=("build", "run"))
