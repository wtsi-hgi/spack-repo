# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringb(RPackage):
	"""Convenient Base R String Handling

	Base R already ships with string handling capabilities 'out-
    of-the-box' but lacks streamlined function names and workflow. The
    'stringi' ('stringr') package on the other hand has well named functions,
    extensive Unicode support and allows for a streamlined workflow. On the other
    hand it adds dependencies and regular expression interpretation between base R
    functions and 'stringi' functions might differ. This packages aims at providing
    a solution to the use case of unwanted dependencies on the one hand but the need
    for streamlined text processing on the other. The packages' functions are solely
    based on wrapping base R functions into 'stringr'/'stringi' like function names.
    Along the way it adds one or two extra functions and last but not least provides
    all functions as generics, therefore allowing for adding methods for other text
    structures besides plain character vectors.
	"""
	
	homepage = "https://github.com/petermeissner/stringb"
	cran = "stringb" 

	version("0.1.17", md5="dbb415c0f468c82350d887128fc4c206")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
