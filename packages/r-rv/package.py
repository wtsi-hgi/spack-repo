# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRv(RPackage):
	"""Simulation-Based Random Variable Objects

	Implements a simulation-based random variable class and a suite of
  methods for extracting parts of random vectors, calculating extremes of random
  vectors, and generating random vectors under a variety of distributions 
  following Kerman and Gelman (2007) <doi:10.1007/s11222-007-9020-4>. 
	"""
	
	homepage = "https://github.com/jsta/rv"
	cran = "rv" 

	version("2.3.5", md5="2b32ab7d8b5fb644b74fb1915d4f9b32")

	depends_on("r@2.15.1:", type=("build", "run"))
