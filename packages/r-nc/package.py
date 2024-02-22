# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNc(RPackage):
	"""Named Capture to Data Tables

	User-friendly functions for extracting a data
 table (row for each match, column for each group)
 from non-tabular text data using regular expressions,
 and for melting columns that match a regular expression.
 Patterns are defined using a readable syntax
 that makes it easy to build complex patterns
 in terms of simpler, re-usable sub-patterns.
 Named R arguments are translated to column names
 in the output; capture groups without names are used
 internally in order to provide a standard interface
 to three regular expression 'C' libraries
 ('PCRE', 'RE2', 'ICU').
 Output can also include numeric columns via
 user-specified type conversion functions.
	"""
	
	homepage = "https://github.com/tdhock/nc"
	cran = "nc" 

	version("2024.2.21", md5="6f28e724c6c122a618114b4e360e06b4")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-data-table@1.15:", type=("build", "run"))
