# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhonenumber(RPackage):
	"""Convert Letters to Numbers and Back as on a Telephone Keypad

	Convert English letters to numbers or numbers to English
    letters as on a telephone keypad. When converting letters to numbers,
    a character vector is returned with "A," "B," or "C" becoming 2, "D,"
    "E", or "F" becoming 3, etc. When converting numbers to letters, a
    character vector is returned with multiple elements (i.e., "2" becomes
    a vector of "A," "B," and "C").
	"""
	
	homepage = "https://stevemyles.site/phonenumber/"
	cran = "phonenumber" 

	version("0.2.3", md5="fa2072465d0f3c16b0a90464e5000bab")

	depends_on("r@3.1.3:", type=("build", "run"))
