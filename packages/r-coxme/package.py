# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxme(RPackage):
	"""Mixed Effects Cox Models

	Fit Cox proportional hazards models containing both 
 fixed and random effects.  The random effects can have a general form, of which
 familial interactions (a "kinship" matrix) is a particular special case. 
 Note that the simplest case of a mixed effects Cox model, i.e. a single random 
 per-group intercept, is also called a "frailty" model.  The approach is based
 on Ripatti and Palmgren, Biometrics 2002.
	"""
	
	cran = "coxme" 

	version("2.2-20", md5="abdedf5f369bb583ee224f654fec8323")

	depends_on("r-survival@2.36.14:", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))
