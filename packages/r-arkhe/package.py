# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArkhe(RPackage):
	"""Tools for Cleaning Rectangular Data

	A dependency-free collection of simple functions for cleaning
    rectangular data. This package allows to detect, count and replace
    values or discard rows/columns using a predicate function. In
    addition, it provides tools to check conditions and return informative
    error messages.
	"""
	
	homepage = "https://packages.tesselle.org/arkhe/"
	cran = "arkhe" 

	version("1.6.0", md5="af3d68f7a2218b75522778e31bd9bb8f")

	depends_on("r@3.5:", type=("build", "run"))
