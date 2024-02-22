# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopdom(RPackage):
	"""An Efficient and Deterministic Method for Identifying
Topological Domains in Genomes

	The 'TopDom' method identifies topological domains in genomes from Hi-C sequence data (Shin et al., 2016 <doi:10.1093/nar/gkv1505>).  The authors published an implementation of their method as an R script (two different versions; also available in this package).  This package originates from those original 'TopDom' R scripts and provides help pages adopted from the original 'TopDom' PDF documentation.  It also provides a small number of bug fixes to the original code.
	"""
	
	homepage = "https://github.com/HenrikBengtsson/TopDom"
	cran = "TopDom" 

	version("0.10.1", md5="68a3c8b7b24ef72f6f4fcb264d151cc9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
