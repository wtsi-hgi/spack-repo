# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwt8(RPackage):
	"""Penn World Table (Version 8.x)

	The Penn World Table 8.x provides information on relative levels of
	income, output, inputs, and productivity for 167 countries
	between 1950 and 2011.
	"""
	
	cran = "pwt8" 

	version("8.1-1", md5="2699af9c3078e12100892f38011df53a", url="https://cran.r-project.org/src/contrib/pwt8_8.1-1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
