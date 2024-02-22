# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpindex(RPackage):
	"""Generalized Price and Quantity Indexes

	Tools to build and work with bilateral generalized-mean
    price indexes (and by extension quantity indexes), and indexes composed of
    generalized-mean indexes (e.g., superlative quadratic-mean indexes, GEKS).
    Covers the core mathematical machinery for making bilateral price indexes,
    computing price relatives, detecting outliers, and decomposing indexes,
    with wrapper for all common (and many uncommon) index-number
    formulas. Implements and extends many of the methods in
    Balk (2008, ISBN:978-1-107-40496-0),
    von der Lippe (2001, ISBN:3-8246-0638-0), and the
    CPI manual (2020, ISBN:978-1-51354-298-0).
	"""
	
	homepage = "https://marberts.github.io/gpindex/"
	cran = "gpindex" 

	version("0.6.0", md5="2ba7444c7cd650d5998df83fcb53e374")

	depends_on("r@4:", type=("build", "run"))
