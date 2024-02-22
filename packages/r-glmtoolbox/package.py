# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmtoolbox(RPackage):
	"""Set of Tools to Data Analysis using Generalized Linear Models

	Set of tools for the statistical analysis of data using: (1) normal linear models; (2) generalized linear models; (3) negative binomial regression models as alternative to the Poisson regression models under the presence of overdispersion; (4) beta-binomial and random-clumped binomial regression models as alternative to the binomial regression models under the presence of overdispersion; (5) Zero-inflated and zero-altered regression models to deal with zero-excess in count data; (6) generalized nonlinear models; (7) generalized estimating equations for cluster correlated data.
	"""
	
	homepage = "https://mlgs.netlify.app/"
	cran = "glmtoolbox" 

	version("0.1.10", md5="9f19c708adbd126480b22588989db687")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
