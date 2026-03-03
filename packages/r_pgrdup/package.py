# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgrdup(RPackage):
	"""Discover Probable Duplicates in Plant Genetic Resources
Collections

	Provides functions to aid the identification of probable/possible
    duplicates in Plant Genetic Resources (PGR) collections using
    'passport databases' comprising of information records of each constituent
    sample. These include methods for cleaning the data, creation of a
    searchable Key Word in Context (KWIC) index of keywords associated with
    sample records and the identification of nearly identical records with
    similar information by fuzzy, phonetic and semantic matching of keywords.
	"""
	
	homepage = "https://cran.r-project.org/package=PGRdup"
	cran = "PGRdup" 

	version("0.2.3.9", md5="68b3783854a603d26596b8fe26247d79")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringdist@0.9.4:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
