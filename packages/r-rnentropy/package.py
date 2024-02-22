# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnentropy(RPackage):
	"""Entropy Based Method for the Detection of Significant Variation
in Gene Expression Data

	An implementation of a method based on information theory devised 
    for the identification of genes showing a significant variation of expression
    across multiple conditions. Given expression estimates from any number of 
    RNA-Seq samples and conditions it identifies genes or transcripts with a 
    significant variation of expression across all the conditions studied, 
    together with the samples in which they are over- or under-expressed. 
    Zambelli et al. (2018) <doi:10.1093/nar/gky055>.
	"""
	
	cran = "RNentropy" 

	version("1.2.3", md5="8c281f9e4cbf38a72f65a510bfa30690")

	depends_on("r@2.10:", type=("build", "run"))
