# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlt(RPackage):
	"""Reinforcement Learning Trees

	Random forest with a variety of additional features for regression, classification and survival analysis. 
             The features include: parallel computing with OpenMP, embedded model for selecting the splitting variable,
             based on Zhu, Zeng & Kosorok (2015) <doi:10.1080/01621459.2015.1036994>, subject weight, variable weight, 
             tracking subjects used in each tree, etc.
	"""
	
	homepage = "https://cran.r-project.org/package=RLT"
	cran = "RLT" 

	version("3.2.6", md5="e2d8a50974e5d250f76b358c39da8077")

