# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmtools(RPackage):
	"""Multi-Level Model Assessment Kit

	Multilevel models (mixed effects models) are the statistical tool of choice for analyzing multilevel data (Searle et al, 2009). These models account for the correlated nature of observations within higher level units by adding group-level error terms that augment the singular residual error of a standard OLS regression. Multilevel and mixed effects models often require specialized data pre-processing and further post-estimation derivations and graphics to gain insight into model results. The package presented here, 'mlmtools', is a suite of pre- and post-estimation tools for multilevel models in 'R'. Package implements post-estimation tools designed to work with models estimated using 'lme4''s (Bates et al., 2014) lmer() function, which fits linear mixed effects regression models. Searle, S. R., Casella, G., & McCulloch, C. E. (2009, ISBN:978-0470009598). Bates, D., Mächler, M., Bolker, B., & Walker, S. (2014) <doi:10.18637/jss.v067.i01>.
	"""
	
	cran = "mlmtools" 

	version("1.0.2", md5="a0d9060a7b003375943c038b66fd31df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
