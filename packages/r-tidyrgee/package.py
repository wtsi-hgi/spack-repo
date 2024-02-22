# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyrgee(RPackage):
	"""'tidyverse' Methods for 'Earth Engine'

	Provides 'tidyverse' methods for wrangling
    and analyzing 'Earth Engine' <https://earthengine.google.com/> data. These methods help the user with filtering, 
    joining and summarising 'Earth Engine' image collections.
	"""
	
	homepage = "https://github.com/r-tidy-remote-sensing/tidyrgee"
	cran = "tidyrgee" 

	version("0.1.0", md5="e7cafaef2be5bb3f37c8eb99e2d097d8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reticulate@1.24:", type=("build", "run"))
	depends_on("r-rgee", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
