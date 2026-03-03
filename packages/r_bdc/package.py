# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdc(RPackage):
	"""Biodiversity Data Cleaning

	It brings together several aspects of biodiversity
    data-cleaning in one place. 'bdc' is organized in thematic modules
    related to different biodiversity dimensions, including 1) Merge
    datasets: standardization and integration of different datasets; 2)
    Pre-filter: flagging and removal of invalid or non-interpretable
    information, followed by data amendments; 3) Taxonomy: cleaning,
    parsing, and harmonization of scientific names from several taxonomic
    groups against taxonomic databases locally stored through the
    application of exact and partial matching algorithms; 4) Space:
    flagging of erroneous, suspect, and low-precision geographic
    coordinates; and 5) Time: flagging and, whenever possible, correction
    of inconsistent collection date. In addition, it contains
    features to visualize, document, and report data quality – which is
    essential for making data quality assessment transparent and
    reproducible. The reference for the methodology is Bruno et al. (2022)
    <doi:10.1111/2041-210X.13868>.
	"""
	
	homepage = "https://brunobrr.github.io/bdc/"
	cran = "bdc" 

	version("1.1.4", md5="4910f45d98b0a2ac9bb0bee7bf6365ae")

	depends_on("r-coordinatecleaner", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rgnparser", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sf@1.0.5:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-taxadb@0.1.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
