# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodebook(RPackage):
	"""Automatic Codebooks from Metadata Encoded in Dataset Attributes

	Easily automate the following tasks to describe data frames:
		Summarise the distributions, and labelled missings of variables graphically
		and using descriptive statistics.
		For surveys, compute and summarise reliabilities (internal consistencies, 
		retest, multilevel) for psychological scales.
		Combine this information with metadata (such as item labels and labelled 
		values) that is derived from R attributes.
		To do so, the package relies on 'rmarkdown' partials, so you can generate 
		HTML, PDF, and Word documents. 
		Codebooks are also available as tables (CSV, Excel, etc.) and in JSON-LD, so
		that search engines can find your data and index the metadata.
		The metadata are also available at your fingertips via RStudio Addins.
	"""
	
	homepage = "https://github.com/rubenarslan/codebook"
	cran = "codebook" 

	version("0.9.2", md5="fca0d41d0e7f4a9b21d839ebfba8ea14")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rmdpartials", type=("build", "run"))
	depends_on("r-forcats@0.4:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-haven@2.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-likert", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-skimr@2.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
