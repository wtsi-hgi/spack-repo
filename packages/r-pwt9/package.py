# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwt9(RPackage):
	"""Penn World Table (Version 9.x)

	The Penn World Table 9.x (<http://www.ggdc.net/pwt/>) provides information
	on relative levels of income, output, inputs, and productivity
	for 182 countries between 1950 and 2017.
	"""
	
	cran = "pwt9" 

	version("9.1-0", md5="d65ef8b90ccb42c2439515386fe2fb8f", url="https://cran.r-project.org/src/contrib/pwt9_9.1-0.tar.gz")

	depends_on("r@3:", type=("build", "run"))
