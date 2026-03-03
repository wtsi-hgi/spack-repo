# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteor(RPackage):
	"""Meteorological Data Manipulation

	A set of functions for weather and climate data manipulation, and other helper functions, to support dynamic ecological modeling, particularly crop and crop disease modeling.
	"""
	
	cran = "meteor" 

	version("0.4-5", md5="e36f1179f3e6653632c331e880dc8186")

	depends_on("r-rcpp", type=("build", "run"))
