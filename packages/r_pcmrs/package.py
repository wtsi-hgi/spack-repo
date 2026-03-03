# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcmrs(RPackage):
	"""Model Response Styles in Partial Credit Models

	Implementation of PCMRS (Partial Credit Model with Response Styles) as proposed in by Tutz, Schauberger and Berger (2018) <doi:10.1177/0146621617748322> .  PCMRS is an extension of the regular partial credit model. PCMRS allows for an additional person parameter that characterizes the response style of the person. By taking the response style into account, the estimates of the item parameters are less biased than in partial credit models.
	"""
	
	cran = "PCMRS" 

	version("0.1-4", md5="43201dcfc28f1111ea2e4a9874d5bfc9")

	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
