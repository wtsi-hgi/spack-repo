# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmevpc(RPackage):
	"""Visual Model Checking for Nonlinear Mixed Effect Model

	Various visual and numerical diagnosis methods for the nonlinear mixed effect model, including visual predictive checks, numerical predictive checks, and coverage plots (Karlsson and Holford, 2008, <https://www.page-meeting.org/?abstract=1434>).
	"""
	
	cran = "nlmeVPC" 

	version("2.6", md5="6b0e42f88078a65851e34df2fcc306f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
