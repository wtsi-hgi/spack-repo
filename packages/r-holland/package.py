# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHolland(RPackage):
	"""Statistics for Holland's Theory of Vocational Choice

	Offers a convenient way to compute parameters 
    in the framework of the theory of vocational choice introduced by
    J.L. Holland, (1997). A comprehensive summary to this theory 
    of vocational choice is given in Holland, J.L. (1997). Making vocational
    choices. A theory of vocational personalities and work environments. 
    Lutz, FL: Psychological Assessment.
	"""
	
	cran = "holland" 

	version("0.1.2-1", md5="4fd26217e419b38b5aae77014ded27b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
