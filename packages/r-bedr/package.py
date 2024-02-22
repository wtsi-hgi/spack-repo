# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBedr(RPackage):
	"""Genomic Region Processing using Tools Such as 'BEDTools',
'BEDOPS' and 'Tabix'

	Genomic regions processing using open-source command line tools such as 'BEDTools', 'BEDOPS' and 'Tabix'. 
  These tools offer scalable and efficient utilities to perform genome arithmetic e.g indexing, formatting and merging.
  bedr API enhances access to these tools as well as offers additional utilities for genomic regions processing.
	"""
	
	cran = "bedr" 

	version("1.0.7", md5="64626c04a41a4ad2f5f56d430dab24fe")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-testthat@0.7.1:", type=("build", "run"))
	depends_on("r-venndiagram@1.6.4:", type=("build", "run"))
	depends_on("r-data-table@1.8.11:", type=("build", "run"))
	depends_on("r-r-utils@2.0.2:", type=("build", "run"))
	depends_on("r-yaml@2.1.10:", type=("build", "run"))
