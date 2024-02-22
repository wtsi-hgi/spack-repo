# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnockoffscreen(RPackage):
	"""Whole-Genome Sequencing Data Analysis via Knockoff Statistics

	Functions for identification of putative causal loci in whole-genome sequencing data. The functions allow genome-wide association scan. It also includes an efficient knockoff generator for genetic data.
	"""
	
	cran = "KnockoffScreen" 

	version("0.3.0", md5="2710eb338f61d341322bfb403c9987e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-seqminer", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-spatest", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
