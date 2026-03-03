# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixl(RPackage):
	"""Simulated Maximum Likelihood Estimation of Mixed Logit Models
for Large Datasets

	Specification and estimation of multinomial logit
    models.  Large datasets and complex models are supported, with an
    intuitive syntax.  Multinomial Logit Models, Mixed models, random
    coefficients and Hybrid Choice are all supported.  For more
    information, see Molloy et al. (2021) <https://www.research-collection.ethz.ch/handle/20.500.11850/477416>.
	"""
	
	homepage = "https://github.com/joemolloy/fast-mixed-mnl"
	cran = "mixl" 

	version("1.3.4", md5="da4c48f0177364c0b78f56ee7a61e99a")

	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rcpp@0.12.19:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
