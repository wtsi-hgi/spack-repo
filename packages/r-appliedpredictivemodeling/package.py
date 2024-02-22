# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppliedpredictivemodeling(RPackage):
	"""Functions and Data Sets for 'Applied Predictive Modeling'

	A few functions and several data set for the Springer book 'Applied Predictive Modeling'.
	"""
	
	homepage = "http://appliedpredictivemodeling.com/"
	cran = "AppliedPredictiveModeling" 

	version("1.1-7", md5="a98e07acde110af11f999aef928e1e29")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-corelearn", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
