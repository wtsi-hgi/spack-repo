# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAricode(RPackage):
	"""Efficient Computations of Standard Clustering Comparison
Measures

	Implements an efficient O(n) algorithm based on bucket-sorting for 
    fast computation of standard clustering comparison measures. Available measures
    include adjusted Rand index (ARI), normalized information distance (NID), 
    normalized mutual information (NMI), adjusted mutual information (AMI), 
    normalized variation information (NVI) and entropy, as described in Vinh et al (2009) 
    <doi:10.1145/1553374.1553511>. Include AMI (Adjusted Mutual Information) since version 0.1.2, 
    a modified version of ARI (MARI), as described in Sundqvist et al. <doi:10.1007/s00180-022-01230-7> 
    and simple Chi-square distance since version 1.0.0.
	"""
	
	homepage = "https://github.com/jchiquet/aricode"
	cran = "aricode" 

	version("1.0.3", md5="7569d0f90f7f2c6186da45abc28869a7")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
