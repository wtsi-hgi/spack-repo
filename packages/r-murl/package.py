# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMurl(RPackage):
	"""Mailmerge using R, LaTeX, and the Web

	Provides mailmerge methods for reading spreadsheets of addresses and other relevant information to create standardized but customizable letters.  Provides a method for mapping US ZIP codes, including those of letter recipients.  Provides a method for parsing and processing html code from online job postings of the American Political Science Association.
	"""
	
	homepage = "https://www.ryantmoore.org/software.murl.html"
	cran = "muRL" 

	version("0.1-13", md5="0e9f939ca87ed1a91d35916cb75aef18")

	depends_on("r-maps", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
