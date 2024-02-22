# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmisc(RPackage):
	"""Adrian Dusa's Miscellaneous

	Contains functions used across packages 'DDIwR', 'QCA' and 'venn'.
    Interprets and translates, factorizes and negates SOP - Sum of Products
    expressions, for both binary and multi-value crisp sets, and extracts
    information (set names, set values) from those expressions. Other functions
    perform various other checks if possibly numeric (even if all numbers reside
    in a character vector) and coerce to numeric, or check if the numbers are
    whole. It also offers, among many others, a highly versatile recoding
    routine and some more flexible alternatives to the base functions 'with()'
    and 'within()'.
    SOP simplification functions in this package use related minimization from
    package 'QCA', which is recommended to be installed despite not being listed
    in the Imports field, due to circular dependency issues.
	"""
	
	homepage = "https://github.com/dusadrian/admisc"
	cran = "admisc" 

	version("0.34", md5="b96b64574ff518294216d699bee81903")

	depends_on("r@3.5:", type=("build", "run"))
