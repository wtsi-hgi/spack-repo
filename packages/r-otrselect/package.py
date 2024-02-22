# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtrselect(RPackage):
	"""Variable Selection for Optimal Treatment Decision

	A penalized regression framework that can simultaneously estimate 
    the optimal treatment strategy and identify important variables. 
    Appropriate for either censored or uncensored continuous response.
	"""
	
	cran = "OTRselect" 

	version("1.2", md5="578e52270276807dadbe1d63c80951f6")

	depends_on("r-lars", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
