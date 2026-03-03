# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrf(RPackage):
	"""Conditional Random Fields

	Implements modeling and computational tools for conditional
    random fields (CRF) model as well as other probabilistic undirected
    graphical models of discrete data with pairwise and unary potentials.
	"""
	
	homepage = "https://github.com/wulingyun/CRF"
	cran = "CRF" 

	version("0.4-3", md5="6ba8011e6924ef8a0beea94bf6bf7dd5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
