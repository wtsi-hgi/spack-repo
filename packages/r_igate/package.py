# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgate(RPackage):
	"""Guided Analytics for Testing Manufacturing Parameters

	An implementation of the initial guided analytics for parameter testing and
    controlband extraction framework. Functions are available for continuous and 
    categorical target variables as well as for generating standardized reports of the
    conducted analysis. See <https://github.com/stefan-stein/igate> for more information
    on the technology.
	"""
	
	homepage = "https://github.com/stefan-stein/igate"
	cran = "igate" 

	version("0.3.3", md5="0b9e9b5b60507a8fe1bdab30ca5d673e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
