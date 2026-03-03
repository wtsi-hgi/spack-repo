# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoplump(RPackage):
	"""Permutation Test for Some Positive and Many Zero Responses

	Calculates permutation tests that can be powerful for comparing two groups with some positive but many zero responses (see Follmann, Fay, and Proschan <DOI:10.1111/j.1541-0420.2008.01131.x>).
	"""
	
	cran = "choplump" 

	version("1.1.2", md5="affb7ef5e760539932783f754ca3676a")

	depends_on("r@2.5:", type=("build", "run"))
