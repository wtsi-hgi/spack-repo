# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygate(RPackage):
	"""Add Gate Information to Your Tibble

	It interactively or programmatically label points within custom gates on two dimensions <https://github.com/stemangiola/tidygate>. 
    The information is added to your tibble. It is based on the package 'gatepoints' from Wajid Jawaid (who is also author of this package). The code of 'gatepoints' was nto integrated in 'tidygate'. 
    The benefits are (i) in interactive mode you can draw your gates on extensive 'ggplot'-like scatter plots; 
    (ii) you can draw multiple gates; and (iii) you can save your gates and apply the programmatically.
	"""
	
	homepage = "https://github.com/stemangiola/tidygate"
	cran = "tidygate" 

	version("0.4.10", md5="74f8dee71f31df124798226c0558759f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
