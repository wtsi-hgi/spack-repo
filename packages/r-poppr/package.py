# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoppr(RPackage):
	"""Genetic Analysis of Populations with Mixed Reproduction

	Population genetic analyses for hierarchical analysis of partially
    clonal populations built upon the architecture of the 'adegenet' package. 
    Originally described in Kamvar, Tabima, and Grünwald (2014) 
    <doi:10.7717/peerj.281> with version 2.0 described in Kamvar, Brooks, and 
    Grünwald (2015) <doi:10.3389/fgene.2015.00208>. 
	"""
	
	homepage = "https://grunwaldlab.github.io/poppr/"
	cran = "poppr" 

	version("2.9.6", md5="fc2e174303fa162c3c969fee31dca4d0")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ape@3.1.1:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-polysat", type=("build", "run"))
	depends_on("r-dplyr@0.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
