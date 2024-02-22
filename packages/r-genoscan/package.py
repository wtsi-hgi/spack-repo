# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenoscan(RPackage):
	"""A Genome-Wide Scan Statistic Framework for Whole-Genome Sequence
Data Analysis

	Functions for whole-genome sequencing studies, including genome-wide scan, candidate region scan and single window test.
	"""
	
	cran = "GenoScan" 

	version("0.1", md5="76aeda12f4fe616bd08ea3a5ba46959f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-seqminer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
