# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdapregex(RPackage):
	"""Regular Expression Removal, Extraction, and Replacement Tools

	A collection of regular expression tools associated with
        the 'qdap' package that may be useful outside of the context of
        discourse analysis. Tools include
        removal/extraction/replacement of abbreviations, dates, dollar
        amounts, email addresses, hash tags, numbers, percentages,
        citations, person tags, phone numbers, times, and zip codes.
	"""
	
	homepage = "https://github.com/trinker/qdapRegex"
	cran = "qdapRegex" 

	version("0.7.8", md5="c5c21c986834e64e87a44891614f0196")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringi@0.5.5:", type=("build", "run"))
