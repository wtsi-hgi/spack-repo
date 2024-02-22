# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarray(RPackage):
	"""Generalized Array Arithmetic for Ragged Arrays with Named
Margins

	Organize a so-called ragged array as generalized arrays, which
	is simply an array with sub-dimensions denoting the subdivision of
	dimensions (grouping of members within dimensions).
	By the margins (names of dimensions and sub-dimensions) in generalized
	arrays, operators and utility functions provided in this package
	automatically match the margins,
	doing map-reduce style parallel computation
	along margins.  Generalized arrays are also cooperative to R's native
	functions that work on simple arrays.
	"""
	
	cran = "garray" 

	version("1.1.2", md5="f61f98946889ce70ca54da777409083f")

	depends_on("r@3.4:", type=("build", "run"))
