# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastqcr(RPackage):
	"""Quality Control of Sequencing Data

	'FASTQC' is the most widely used tool for evaluating the quality of high throughput sequencing data.  
    It produces, for each sample, an html report and a compressed file containing the raw data. 
    If you have hundreds of samples, you are not going to open up each 'HTML' page. 
    You need some way of looking at these data in aggregate. 
    'fastqcr' Provides helper functions to easily parse, aggregate and analyze 
    'FastQC' reports for large numbers of samples. It provides a convenient solution for building 
    a 'Multi-QC' report, as well as, a 'one-sample' report with result interpretations.
	"""
	
	homepage = "https://rpkgs.datanovia.com/fastqcr/index.html"
	cran = "fastqcr" 

	version("0.1.3", md5="513ea702c44495a870e92ac44462af16")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-rmarkdown@1.4:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
