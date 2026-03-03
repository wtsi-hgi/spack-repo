# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJlpm(RPackage):
	"""Joint Latent Process Models

	Estimation of extended joint models with shared random effects. Longitudinal data are handled in latent process models for continuous (Gaussian or curvilinear) and ordinal outcomes while proportional hazard models are used for the survival part. We propose a frequentist approach using maximum likelihood estimation. See Saulnier et al, 2022 <doi:10.1016/j.ymeth.2022.03.003>.
	"""
	
	cran = "JLPM" 

	version("1.0.2", md5="7d41344f46b8c33f42d7a1116f836db9")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lcmm", type=("build", "run"))
	depends_on("r-survival@2.37.2:", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-marqlevalg@2.0.6:", type=("build", "run"))
