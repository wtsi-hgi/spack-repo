# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcros(RPackage):
	"""A Method to Search for Differentially Expressed Genes and to
Detect Recurrent Chromosomal Copy Number Aberrations

	A fold change rank based method is presented to search for genes with changing
             expression and to detect recurrent chromosomal copy number aberrations. This 
             method may be useful for high-throughput biological data (micro-array, sequencing, ...).
             Probabilities are associated with genes or probes in the data set and there is no
             problem of multiple tests when using this method. For array-based comparative genomic
             hybridization data, segmentation results are obtained by merging the significant
             probes detected.
	"""
	
	cran = "fcros" 

	version("1.6.1", md5="76248f38c69b855d5b097b990783ef06")

	depends_on("r@3.1:", type=("build", "run"))
