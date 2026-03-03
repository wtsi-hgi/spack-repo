# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMccmeiv(RPackage):
	"""Analysis of Matched Case Control Data with a Mismeasured
Exposure that is Accompanied by Instrumental Variables

	Applying the methodology from Manuel et al. to estimate parameters using a matched 
    case control data with a mismeasured exposure variable that is accompanied by 
    instrumental variables (Submitted). 
	"""
	
	cran = "mccmeiv" 

	version("2.1", md5="e1eeda24f04b0c5e36c3b750895dec8e")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
