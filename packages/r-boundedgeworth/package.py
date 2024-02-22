# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoundedgeworth(RPackage):
	"""Bound on the Error of the First-Order Edgeworth Expansion

	Computes uniform bounds on the distance between
  the cumulative distribution function of a standardized sum
  of random variables and its first-order Edgeworth expansion,
  following the article Derumigny, Girard, Guyonvarch (2021)
  <arXiv:2101.05780>.
	"""
	
	cran = "BoundEdgeworth" 

	version("0.1.2.1", md5="9d0f1474080e5b94bb1b72005f466f68")

	depends_on("r-expint", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
