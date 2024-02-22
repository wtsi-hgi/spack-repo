# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsdals(RPackage):
	"""Datasets for Introduction to Statistical Data Analysis for the
Life Sciences

	Provides datasets for the book "Introduction to Statistical Data Analysis for the Life Sciences, Second edition" by Ekstrøm and Sørensen (2014).
	"""
	
	cran = "isdals" 

	version("3.0.1", md5="d0d2e37d2d3ea205160a8e3a2d304d11")

