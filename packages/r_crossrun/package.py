# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossrun(RPackage):
	"""Joint Distribution of Number of Crossings and Longest Run

	Joint distribution of number of crossings and the 
  longest run in a series of independent Bernoulli trials. The
  computations uses an iterative procedure where computations 
  are based on results from shorter series. The procedure 
  conditions on the start value and partitions by further 
  conditioning on the position of the first crossing (or none).
	"""
	
	homepage = "https://github.com/ToreWentzel-Larsen/crossrun"
	cran = "crossrun" 

	version("0.1.1", md5="9ba9d1862d5083a05178f07e6addb2b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmpfr@0.7.1:", type=("build", "run"))
