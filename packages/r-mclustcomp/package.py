# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMclustcomp(RPackage):
	"""Measures for Comparing Clusters

	Given a set of data points, a clustering is defined as a disjoint partition
    where each pair of sets in a partition has no overlapping elements. 
    This package provides 25 methods that play a role somewhat similar to 
    distance or metric that measures similarity of two clusterings - or partitions.
    For a more detailed description, see Meila, M. (2005) <doi:10.1145/1102351.1102424>.
	"""
	
	cran = "mclustcomp" 

	version("0.3.3", md5="4e83a5125dae0ec5754bd0a76ed240c5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
