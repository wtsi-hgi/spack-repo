# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgiraphextra(RPackage):
	"""Make Interactive 'ggplot2'. Extension to 'ggplot2' and 'ggiraph'

	Collection of functions to enhance 'ggplot2' and 'ggiraph'. Provides functions for exploratory plots.
    All plot can be a 'static' plot or an 'interactive' plot using 'ggiraph'.
	"""
	
	homepage = "https://github.com/cardiomoon/ggiraphExtra"
	cran = "ggiraphExtra" 

	version("0.3.0", md5="d183239e49f60207ffea73efaffad916")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-ggiraph@0.3.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mycor", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
