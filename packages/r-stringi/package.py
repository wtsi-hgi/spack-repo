# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringi(RPackage):
	"""Character String Processing Facilities.

	A multitude of character string/text/natural language processing tools:
	pattern searching (e.g., with 'Java'-like regular expressions or the
	'Unicode' collation algorithm), random string generation, case mapping,
	string transliteration, concatenation, sorting, padding, wrapping, Unicode
	normalisation, date-time formatting and parsing, and many more.  They are
	fast, consistent, convenient, and - owing to the use of the 'ICU'
	(International Components for Unicode) library - portable across all
	locales and platforms."""

	cran = "stringi"

	license("custom")

	version("1.8.3", md5="ebc7252eb0269ff7aae2966e4a85b4d6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("icu4c@61:", type=("build", "link", "run"))
	# since version 1.6.1 there is also a SystemRequirement on C++11
