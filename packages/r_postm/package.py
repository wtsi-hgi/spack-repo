# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostm(RPackage):
	"""Phylogeny-Guided OTU-Specific Association Test for Microbiome
Data

	Implements the Phylogeny-Guided Microbiome OTU-Specific Association 
    Test method, which boosts the testing power by adaptively borrowing 
    information from phylogenetically close OTUs (operational taxonomic units)
    of the target OTU. This method
    is built on a kernel machine regression framework and allows for flexible 
    modeling of complex microbiome effects, adjustments for covariates, and 
    can accommodate both continuous and binary outcomes. 
	"""
	
	cran = "POSTm" 

	version("1.3", md5="ec81f9a4739ca350fec198fce871a213")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
