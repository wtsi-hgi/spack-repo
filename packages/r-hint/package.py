# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHint(RPackage):
	"""Tools for Hypothesis Testing Based on Hypergeometric
Intersection Distributions

	Hypergeometric Intersection distributions are a
    broad group of distributions that describe the probability of picking
    intersections when drawing independently from two (or more) urns
    containing variable numbers of balls belonging to the same n
    categories. <arXiv:1305.0717>.
	"""
	
	homepage = "https://github.com/alextkalinka/hint"
	cran = "hint" 

	version("0.1-3", md5="54f1cd0822813aa3d4d9f1cb7310e3ad")

