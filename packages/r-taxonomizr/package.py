# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxonomizr(RPackage):
	"""Functions to Work with NCBI Accessions and Taxonomy

	Functions for assigning taxonomy to NCBI accession numbers and taxon IDs based on NCBI's accession2taxid and taxdump files. This package allows the user to download NCBI data dumps and create a local database for fast and local taxonomic assignment.
	"""
	
	cran = "taxonomizr" 

	version("0.10.6", md5="58acae0ed99c42b404cd54c098128b74")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl@5:", type=("build", "run"))
