# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCream(RPackage):
	"""Clustering of Genomic Regions Analysis Method

	Provides a new method for identification of clusters of genomic
 regions within chromosomes. Primarily, it is used for calling clusters of 
 cis-regulatory elements (COREs). 'CREAM' uses genome-wide maps of genomic regions
 in the tissue or cell type of interest, such as those generated from chromatin-based 
 assays including DNaseI, ATAC or ChIP-Seq. 'CREAM' considers proximity of the elements 
 within chromosomes of a given sample to identify COREs in the following steps:
 1) It identifies window size or the maximum allowed distance between the elements 
 within each CORE, 2) It identifies number of elements which should be clustered 
 as a CORE, 3) It calls COREs, 4) It filters the COREs with lowest order which 
 does not pass the threshold considered in the approach.
	"""
	
	homepage = "https://github.com/bhklab/CREAM"
	cran = "CREAM" 

	version("1.1.1", md5="f36d16c05551649b7dad16904e0056d2")

	depends_on("r@3.3:", type=("build", "run"))
