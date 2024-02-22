# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSievetest(RPackage):
	"""Laboratory Sieve Test Reporting Functions

	Functions for making particle-size analysis. Sieve tests are widely used to obtain particle-size distribution of powders or granular materials.
	"""
	
	cran = "sievetest" 

	version("1.2.3", md5="760758c98f4644e240431e4ccf6a9a8c")

	depends_on("r@3.1:", type=("build", "run"))
