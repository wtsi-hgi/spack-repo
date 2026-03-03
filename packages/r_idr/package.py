# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdr(RPackage):
	"""Irreproducible Discovery Rate

	This is a package for estimating the copula mixture model and plotting correspondence curves. Details are in "Measuring reproducibility of high-throughput experiments" (2011), Annals of Applied Statistics, Vol. 5, No. 3, 1752-1779, by Li, Brown, Huang, and Bickel. 
	"""
	
	cran = "idr" 

	version("1.3", md5="d3fcfef19b12cd9c0867fd607ab7ca5b")

