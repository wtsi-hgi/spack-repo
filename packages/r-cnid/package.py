# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnid(RPackage):
	"""Get Basic Information from Chinese ID Number

	The Chinese ID number contains a lot of information,
    this package helps you get the date of birth, age, age based
    on year, gender, region, zodiac, constellation information from
    the Chinese ID number.
	"""
	
	homepage = "https://gitlab.com/chuxinyuan/cnid"
	cran = "CNID" 

	version("1.3.1", md5="4b0bd1dd2855110d8496cbe5fc6d3e2b")

	depends_on("r@3:", type=("build", "run"))
