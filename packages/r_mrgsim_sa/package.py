# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrgsimSa(RPackage):
	"""Sensitivity Analysis with 'mrgsolve'

	Perform sensitivity analysis on ordinary differential equation 
    based models, including ad-hoc graphical analyses based on structured 
    sequences of parameters as well as local sensitivity analysis. Functions 
    are provided for creating inputs, simulating scenarios and plotting outputs.
	"""
	
	homepage = "https://github.com/kylebaron/mrgsim.sa"
	cran = "mrgsim.sa" 

	version("0.2.0", md5="df8ac143e107ffd32e53b2d21971b190")

	depends_on("r-mrgsolve", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
