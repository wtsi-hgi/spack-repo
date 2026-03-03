# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasr(RPackage):
	"""Bayesian Psychometric Measurement Using 'Stan'

	Estimate diagnostic classification models (also called cognitive
    diagnostic models) with 'Stan'. Diagnostic classification models are 
    confirmatory latent class models, as described by Rupp et al.
    (2010, ISBN: 978-1-60623-527-0). Automatically generate 'Stan' code for the
    general loglinear cognitive diagnostic diagnostic model proposed by
    Henson et al. (2009) <doi:10.1007/s11336-008-9089-5> and other subtypes that
    introduce additional model constraints. Using the generated 'Stan' code,
    estimate the model evaluate the model's performance using model fit indices,
    information criteria, and reliability metrics.
	"""
	
	homepage = "https://measr.info"
	cran = "measr" 

	version("1.0.0", md5="807ffbe10b01c71321230ca8417b11fc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dcm2", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
