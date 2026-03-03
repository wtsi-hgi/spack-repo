# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwt10(RPackage):
	"""Penn World Table (Version 10.x)

	The Penn World Table 10.x (<https://www.rug.nl/ggdc/productivity/pwt/>) provides information
	on relative levels of income, output, input, and productivity
	for 183 countries between 1950 and 2019.
	"""
	
	cran = "pwt10" 

	version("10.01-0", md5="cb35e0265de255b6b7f77a8d3c0a7f7b", url="https://cran.r-project.org/src/contrib/pwt10_10.01-0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
