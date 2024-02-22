# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2shortcode(RPackage):
	"""Shorten Package Function Names

	When creating a package, authors may sometimes struggle with coming up with easy and straightforward function names, and at the same time hoping that other packages do not already have the same function names. In trying to meet this goal, sometimes, function names are not descriptive enough and may confuse the potential users. The purpose of this package is to serve as a package function short form generator and also provide shorthand names for other functions. Having this package will entice authors to create long function names without the fear of users not wanting to use their packages because of the long names. In a way, everyone wins - the authors can use long descriptive function names, and the users can use this package to make short functions names while still using the package in question.
	"""
	
	homepage = "https://github.com/oobianom/r2shortcode"
	cran = "r2shortcode" 

	version("0.1", md5="cfa3f120015bd80fccf8b338aa9febc5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
