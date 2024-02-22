# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrelliscopejs(RPackage):
	"""Create Interactive Trelliscope Displays

	Trelliscope is a scalable, flexible, interactive approach to visualizing data (Hafen, 2013 <doi:10.1109/LDAV.2013.6675164>). This package provides methods that make it easy to create a Trelliscope display specification for TrelliscopeJS. High-level functions are provided for creating displays from within 'tidyverse' or 'ggplot2' workflows. Low-level functions are also provided for creating new interfaces.
	"""
	
	homepage = "https://github.com/hafen/trelliscopejs"
	cran = "trelliscopejs" 

	version("0.2.6", md5="1eafd416afa1992007cbaab6c6858c4e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-distributionutils", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-autocogs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
