# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVmeasur(RPackage):
	"""Quantify the Contractile Nature of Vessels Monitored under an
Operating Microscope

	A variety of tools to allow the quantification of videos of the 
    lymphatic vasculature taken under an operating microscope. Lymphatic vessels
    that have been injected with a variety of blue dyes can be tracked throughout
    the video to determine their width over time. Code is optimised
    for efficient processing of multiple large video files. Functions to calculate
    physiologically relevant parameters and generate graphs from these values 
    are also included.
	"""
	
	cran = "vmeasur" 

	version("0.1.4", md5="156ac8b9aeb82bc76b0dcca4aea084ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-av", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-svdialogs", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
