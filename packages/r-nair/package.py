# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNair(RPackage):
	"""Network Analysis of Immune Repertoire

	Pipelines for studying the adaptive immune repertoire of T cells 
    and B cells via network analysis based on receptor sequence similarity. 
    Relate clinical outcomes to immune repertoires based on their network 
    properties, or to particular clusters and clones within a repertoire. 
    Yang et al. (2023) <doi:10.3389/fimmu.2023.1181825>.
	"""
	
	homepage = "https://mlizhangx.github.io/Network-Analysis-for-Repertoire-Sequencing-/"
	cran = "NAIR" 

	version("1.0.4", md5="a7e3d1705c0d54e2df6982deb1aba44b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.8:", type=("build", "run"))
