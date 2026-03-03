# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkbtools(RPackage):
	"""Manipulate and Explore UK Biobank Data

	A set of tools to create a UK Biobank <http://www.ukbiobank.ac.uk/> dataset from a UKB fileset (.tab, .r, .html),
    visualize primary demographic data for a sample subset, query ICD diagnoses,
    retrieve genetic metadata, read and write standard file formats for genetic analyses.
	"""
	
	homepage = "https://kenhanscombe.github.io/ukbtools/"
	cran = "ukbtools" 

	version("0.11.3", md5="bd3fe22723f563d778ac226f4d76d1d7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
