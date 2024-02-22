# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenescape(RPackage):
	"""Simulation of Single Cell RNA-Seq Data with Complex Structure

	Simulating single cell RNA-seq data with complicated structure. This package is developed based on the Splat method (Zappia, Phipson and Oshlack (2017) <doi:10.1186/s13059-017-1305-0>). 'GeneScape' incorporates additional features to simulate single cell RNA-seq data with complicated differential expression and correlation structures, such as sub-cell-types, correlated genes (pathway genes) and hub genes. 
	"""
	
	cran = "GeneScape" 

	version("1.0", md5="ec26ca19c7ae6e9b038892b4fd78689b")

	depends_on("r-mass@7.3.53.1:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
