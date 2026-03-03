# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxonbridge(RPackage):
	"""Create Custom Taxonomies Based on the NCBI Taxonomy and GBIF
Backbone Taxonomy

	The NCBI taxonomy is a popular resource for taxonomic studies but it only contains
    data on species with sequence data whereas the GBIF has a more extensive coverage of
    extinct species. Taxonbridge is useful for the creation and analysis of custom taxonomies
    based on the NCBI taxonomy and GBIF backbone taxonomy.
	"""
	
	homepage = "https://github.com/MoultDB/taxonbridge"
	cran = "taxonbridge" 

	version("1.2.2", md5="8a9c613d04d77dcd536505af287a7131")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rje", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
