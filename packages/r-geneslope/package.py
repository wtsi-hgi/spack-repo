# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneslope(RPackage):
	"""Genome-Wide Association Study with SLOPE

	Genome-wide association study (GWAS) performed with SLOPE,
    short for Sorted L-One Penalized Estimation, a
    method for estimating the vector of coefficients in a linear model.
    In the first step of GWAS, single nucleotide polymorphisms (SNPs) are 
    clumped according to their correlations and distances. 
    Then, SLOPE is performed on the data where each clump has
    one representative.
    Malgorzata Bogdan, Ewout van den Berg, Chiara Sabatti, Weijie Su 
    and Emmanuel Candes (2014) 
    "SLOPE - Adaptive Variable Selection via Convex Optimization" 
    <arXiv:1407.3824>.
	"""
	
	homepage = "https://github.com/psobczyk/geneSLOPE"
	cran = "geneSLOPE" 

	version("0.38.2", md5="1417e3683bbe20a7c371e653ac199aa0")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-slope", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
