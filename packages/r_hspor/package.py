# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHspor(RPackage):
	"""Hidden Smooth Polynomial Regression for Rupture Detection

	Several functions that allow by different methods to infer a piecewise polynomial regression model under regularity constraints, namely continuity or differentiability of the link function. The implemented functions are either specific to data with two regimes, or generic for any number of regimes, which can be given by the user or learned by the algorithm. A paper describing all these methods will be submitted soon. The reference will be added to this file as soon as available. 
	"""
	
	cran = "HSPOR" 

	version("1.1.9", md5="47ff4b459c91440279ab605a198af428")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-npregfast", type=("build", "run"))
