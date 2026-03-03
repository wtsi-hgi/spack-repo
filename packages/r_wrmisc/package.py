# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrmisc(RPackage):
	"""Analyze Experimental High-Throughput (Omics) Data

	The efficient treatment and convenient analysis of experimental high-throughput (omics) data gets facilitated through this collection of diverse functions. 
  Several functions address advanced object-conversions, like manipulating lists of lists or lists of arrays, reorganizing lists to arrays or into separate vectors, merging of multiple entries, etc.  
  Another set of functions provides speed-optimized calculation of standard deviation (sd), coefficient of variance (CV) or standard error of the mean (SEM)  
  for data in matrixes or means per line with respect to additional grouping (eg n groups of replicates). 
  Other functions facilitate dealing with non-redundant information, by indexing unique, adding counters to redundant or eliminating lines with respect redundancy in a given reference-column, etc. 
  Help is provided to identify very closely matching numeric values to generate (partial) distance matrixes for very big data in a memory efficient manner or to reduce the complexity of large data-sets by combining very close values. 
  Many times large experimental datasets need some additional filtering, adequate functions are provided. 
  Batch reading (or writing) of sets of files and combining data to arrays is supported, too. 
  Convenient data normalization is supported in various different modes, parameter estimation via permutations or boot-strap as well as flexible testing of multiple pair-wise combinations using the framework of 'limma' is provided, too.
	"""
	
	cran = "wrMisc" 

	version("1.14.2", md5="3482ffb1c842b52829d13c08515330ef")
	version("1.14.1", md5="0a97a1f9d0e3b48348c1aebebd23846a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
