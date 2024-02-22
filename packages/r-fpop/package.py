# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpop(RPackage):
	"""Segmentation using Optimal Partitioning and Function Pruning

	A dynamic programming algorithm for the fast segmentation of univariate signals into piecewise constant profiles.
  The 'fpop'  package is a wrapper to a C++ implementation of the fpop (Functional Pruning Optimal Partioning) algorithm described in Maidstone et al. 2017
  <doi:10.1007/s11222-016-9636-3>. The problem of detecting changepoints in an univariate sequence is formulated 
  in terms of minimising the mean squared error over segmentations. The fpop algorithm exactly minimizes the mean squared error 
  for a penalty linear in the number of changepoints.
	"""
	
	cran = "fpop" 

	version("2019.08.26", md5="cc572b4be47407f3fccc74f8f8ce5a5d")

