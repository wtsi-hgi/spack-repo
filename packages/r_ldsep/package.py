# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdsep(RPackage):
	"""Linkage Disequilibrium Shrinkage Estimation for Polyploids

	Estimate haplotypic or composite pairwise linkage disequilibrium
    (LD) in polyploids, using either genotypes or genotype likelihoods. 
    Support is provided to estimate the popular measures of LD: the LD 
    coefficient D, the standardized LD coefficient D', and the Pearson 
    correlation coefficient r. All estimates are returned with corresponding 
    standard errors. These estimates and standard errors can then be used
    for shrinkage estimation. The main functions are ldfast(), ldest(), mldest(),
    sldest(), plot.lddf(), format_lddf(), and ldshrink(). Details of the methods
    are available in Gerard (2021a) <doi:10.1111/1755-0998.13349>
    and Gerard (2021b) <doi:10.1038/s41437-021-00462-5>.
	"""
	
	cran = "ldsep" 

	version("2.1.5", md5="d65b7970626f51cc3c06901057365ed0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
