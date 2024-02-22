# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMomentfit(RPackage):
	"""Methods of Moments

	Several classes for moment-based models are defined. The classes are defined for moment conditions derived from a single equation or a system of equations. The conditions can also be expressed as functions or formulas. Several methods are also offered to facilitate the development of different estimation techniques. The methods that are currently provided are the Generalized method of moments (Hansen 1982; <doi:10.2307/1912775>), for single equations and systems of equation, and  the Generalized Empirical Likelihood (Smith 1997; <doi:10.1111/j.0013-0133.1997.174.x>, Kitamura 1997; <doi:10.1214/aos/1069362388>, Newey and Smith 2004; <doi:10.1111/j.1468-0262.2004.00482.x>, and Anatolyev 2005 <doi:10.1111/j.1468-0262.2005.00601.x>). 
	"""
	
	cran = "momentfit" 

	version("0.5", md5="4c9c861db840842f89e783b15f48488e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
