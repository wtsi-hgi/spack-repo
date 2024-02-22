# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankaggregator(RPackage):
	"""Aggregation of (Partial) Ordinal Rankings

	Easily compute an aggregate ranking (also called a median ranking or a
             consensus ranking) according to the axiomatic approach presented
             by Cook et al. (2007). This approach minimises the number of violations
             between all candidate consensus rankings and all input (partial) rankings,
             and draws on a branch and bound algorithm and a heuristic algorithm to
             drastically improve speed. The package also provides an option to bootstrap
             a consensus ranking based on resampling input rankings (with 
             replacement). Input rankings can be either incomplete (partial) or complete.
             Reference: Cook, W.D., Golany, B., Penn, M. and Raviv, T. (2007) <doi:10.1016/j.cor.2005.05.030>.
	"""
	
	cran = "RankAggregator" 

	version("0.0.1", md5="a8cf567e606cfffc2dbb9f8425930547")

	depends_on("r@2.10:", type=("build", "run"))
