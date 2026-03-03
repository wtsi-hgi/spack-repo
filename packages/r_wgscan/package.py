# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWgscan(RPackage):
	"""A Genome-Wide Scan Statistic Framework for Whole-Genome Sequence
Data Analysis

	Functions for the analysis of whole-genome sequencing studies to simultaneously detect the existence, and estimate the locations of association signals at genome-wide scale. The functions allow genome-wide association scan, candidate region scan and single window test.
	"""
	
	cran = "WGScan" 

	version("0.1", md5="522b57e73307f8d46702901d91712e69")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-seqminer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
