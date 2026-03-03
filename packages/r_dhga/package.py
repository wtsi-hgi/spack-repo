# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhga(RPackage):
	"""Differential Hub Gene Analysis

	Identification of hub genes in a gene co-expression network from gene expression data. The differential network analysis for two contrasting conditions leads to the identification of various types of hubs like Housekeeping, Unique to stress (Disease) and Unique to control (Normal) hub genes. 
	"""
	
	cran = "dhga" 

	version("0.1", md5="c99040991cd02c2d6ce6531273c68f10")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
