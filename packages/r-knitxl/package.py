# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnitxl(RPackage):
	"""Generates a Spreadsheet Report from an 'rmarkdown' File

	Convert an R Markdown documents into an '.xlsx' spreadsheet reports
    with the knitxl() function, which works similarly to knit() from the 
    'knitr' package. The generated report can be opened in 'Excel' or similar
    software for further analysis and presentation.
	"""
	
	homepage = "https://github.com/dreanod/knitxl"
	cran = "knitxl" 

	version("0.1.0", md5="21b66b4c86f25422c0810a607d3dd6fe")

	depends_on("r-knitr@1.39:", type=("build", "run"))
	depends_on("r-commonmark@1.8:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-readbitmap@0.1.5:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-xml2@1.3.3:", type=("build", "run"))
	depends_on("r-yaml@2.3.7:", type=("build", "run"))
