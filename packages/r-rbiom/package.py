# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbiom(RPackage):
	"""Read/Write, Transform, and Summarize 'BIOM' Data

	
    A toolkit for working with Biological Observation Matrix ('BIOM') files.
    Features include reading/writing all 'BIOM' formats, rarefaction, alpha
    diversity, beta diversity (including 'UniFrac'), summarizing counts by 
    taxonomic level, and sample subsetting. Standalone functions for 
    reading, writing, and subsetting phylogenetic trees are also provided. 
    All CPU intensive operations are encoded in C with multi-thread support.
	"""
	
	homepage = "https://cmmr.github.io/rbiom/index.html"
	cran = "rbiom" 

	version("1.0.3", md5="c132b75964adfb199f20d1fdc1da67f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
