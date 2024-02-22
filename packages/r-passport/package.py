# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPassport(RPackage):
	"""Travel Smoothly Between Country Name and Code Formats

	Smooths the process of working with country names and codes via 
    powerful parsing, standardization, and conversion utilities arranged in a 
    simple, consistent API. Country name formats include multiple sources 
    including the Unicode Common Locale Data 
    Repository (CLDR, <http://cldr.unicode.org/>) common-sense standardized 
    names in hundreds of languages.
	"""
	
	homepage = "https://github.com/alistaire47/passport"
	cran = "passport" 

	version("0.3.0", md5="db48f257d05d84579a77e7cfd0e86eda")

	depends_on("r@3.1:", type=("build", "run"))
