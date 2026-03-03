# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmer(RPackage):
	"""Fast K-Mer Counting and Clustering for Biological Sequence
Analysis

	Contains tools for rapidly computing distance matrices 
    and clustering large sequence datasets using fast alignment-free 
    k-mer counting and recursive k-means partitioning. 
    See Vinga and Almeida (2003) <doi:10.1093/bioinformatics/btg005> 
    for a review of k-mer counting methods and applications for 
    biological sequence analysis.
	"""
	
	homepage = "http://github.com/shaunpwilkinson/kmer"
	cran = "kmer" 

	version("1.1.2", md5="a1d0d4bbe961c123d71b2d85a742980d")

	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-phylogram", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
