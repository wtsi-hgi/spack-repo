# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterability(RPackage):
	"""Performs Tests for Cluster Tendency of a Data Set

	Test for cluster tendency (clusterability) of a data set.
    The methods implemented - reducing the data set to a single dimension using principal component analysis or computing
    pairwise distances, and performing a multimodality test like the Dip Test or Silverman's Critical Bandwidth Test - 
    are described in Adolfsson, Ackerman, and Brownstein (2019) <doi:10.1016/j.patcog.2018.10.026>. Such methods can inform whether clustering algorithms
    are appropriate for a data set.
	"""
	
	cran = "clusterability" 

	version("0.1.1.0", md5="b0be440a5533e6d07a1c748582bba0d7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
