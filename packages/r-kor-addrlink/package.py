# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKorAddrlink(RPackage):
	"""Matching Address Data to Reference Index

	Matches a data set with semi-structured address data, 
 e.g., street and house number as a concatenated string,
 wrongly spelled street names or non-existing house numbers to a 
 reference index. The methods are specifically designed for German 
 municipalities ('KOR'-community) and German address schemes.
	"""
	
	homepage = "https://git-kor.stadtdo.de"
	cran = "KOR.addrlink" 

	version("1.0.1", md5="5c329bb69d39cb25d734e7ddc135197f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
