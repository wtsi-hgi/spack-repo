# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLhd(RPackage):
	"""Latin Hypercube Designs (LHDs)

	Contains different algorithms and construction methods for optimal Latin hypercube designs (LHDs) with flexible sizes. Our package is comprehensive since it is capable of generating maximin distance LHDs, maximum projection LHDs, and orthogonal and nearly orthogonal LHDs. Detailed comparisons and summary of all the algorithms and construction methods in this package can be found at Hongzhi Wang, Qian Xiao and Abhyuday Mandal (2021) <arXiv:2010.09154>. This package is particularly useful in the area of Design and Analysis of Experiments (DAE). More specifically, design of computer experiments.
	"""
	
	cran = "LHD" 

	version("1.3.3", md5="f70ac69c0072dec6e42742dd38b304d3")

	depends_on("r-numbers", type=("build", "run"))
