# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlinkanalyze(RPackage):
	"""Facilitate Analysis of Proteomic Data from Olink

	A collection of functions to facilitate analysis of proteomic
    data from Olink, primarily NPX data that has been exported from Olink
    Software. The functions also work on QUANT data from
    Olink by log- transforming the QUANT data. The functions are focused
    on reading data, facilitating data wrangling and quality control
    analysis, performing statistical analysis and generating figures to
    visualize the results of the statistical analysis. The goal of this
    package is to help users extract biological insights from proteomic
    data run on the Olink platform.
	"""
	
	homepage = "https://olink.com/"
	cran = "OlinkAnalyze" 

	# Latest CRAN release
	version("4.3.2", sha256="0a54035ae36382cc26e9f4021067ff7f766ad642bc6a5c226a0744891ae20084")
	# Older version retained for compatibility
	version("3.7.0", md5="53bd38935a24a7f5aa208c41321ec6ee")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	# CRAN >= 4.3.2 requires dplyr >= 1.1.1
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	# New in 4.3.2
	depends_on("r-cli@3.6.2:", when="@4.3.2:", type=("build", "run"))
	depends_on("r-data-table", when="@4.3.2:", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	# zip is only a Suggests in 4.3.2 but keeping as a dependency is harmless
	depends_on("r-zip", type=("build", "run"))
