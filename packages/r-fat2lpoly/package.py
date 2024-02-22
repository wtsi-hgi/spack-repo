# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFat2lpoly(RPackage):
	"""Two-Locus Family-Based Association Test with Polytomous Outcome

	Performs family-based association tests with a polytomous outcome under 2-locus and 1-locus models
             defined by some design matrix.  
	"""
	
	homepage = "https://www.cervo.ulaval.ca/pages_perso_chercheurs/bureau_a/"
	cran = "fat2Lpoly" 

	version("1.2.5", md5="22266325fc04c9455dc34eb84adfbcf5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-multgee", type=("build", "run"))
