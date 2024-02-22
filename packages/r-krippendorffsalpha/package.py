# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKrippendorffsalpha(RPackage):
	"""Measuring Agreement Using Krippendorff's Alpha Coefficient

	Provides tools for applying Krippendorff's Alpha methodology <DOI:10.1080/19312450709336664>. Both the customary methodology and Hughes' methodology <DOI:10.48550/arXiv.2210.13265> are supported, the former being preferred for larger datasets, the latter for smaller datasets. The framework supports common and user-defined distance functions, and can accommodate any number of units, any number of coders, and missingness. Interval estimation can be done in parallel for either methodology.
	"""
	
	homepage = "http://www.johnhughes.org"
	cran = "krippendorffsalpha" 

	version("2.0", md5="8b3b69cb6e0470d8e23b213d3125c8c1")

