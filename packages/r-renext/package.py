# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRenext(RPackage):
	"""Renewal Method for Extreme Values Extrapolation

	Peaks Over Threshold (POT) or 'methode du renouvellement'. The
    distribution for the excesses can be chosen, and heterogeneous data
    (including historical data or block data) can be used in a
    Maximum-Likelihood framework. 
	"""
	
	homepage = "https://github.com/IRSN/Renext"
	cran = "Renext" 

	version("3.1-4", md5="cac62a2cbccc0653526ef3ff74e0650f")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
