# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpseg(RPackage):
	"""Piecewise Linear Segmentation by Dynamic Programming

	Piecewise linear segmentation of ordered data by a
        dynamic programming algorithm. The algorithm was developed for time
	series data, e.g. growth curves, and for genome-wide read-count data
        from next generation sequencing, but is broadly applicable.
        Generic implementations of dynamic programming routines allow
        to scan for optimal segmentation parameters and test custom
        segmentation criteria ("scoring functions").
	"""
	
	homepage = "https://gitlab.com/raim/dpseg/"
	cran = "dpseg" 

	version("0.1.1", md5="2317aadc54b844d72e989dd8f9cb9a3f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
