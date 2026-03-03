# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchr(RPackage):
	"""Pattern Matching and Enumerated Types in R

	Inspired by pattern matching and enum types in Rust
    and many functional programming languages, this package offers
    an updated version of the 'switch' function called 'Match' that
    accepts atomic values, functions, expressions, and enum variants.
    Conditions and return expressions are separated by '->' and 
    multiple conditions can be associated with the same return expression
    using '|'. 'Match' also includes support for 'fallthrough'. The 
    package also replicates the Result and Option enums from Rust.
	"""
	
	cran = "matchr" 

	version("0.1.0", md5="46b68109a51a90dfa63b54bf87eaacd1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
