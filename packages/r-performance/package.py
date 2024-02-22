# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerformance(RPackage):
	"""Assessment of Regression Models Performance

	Utilities for computing measures to assess model quality,
    which are not directly provided by R's 'base' or 'stats' packages.
    These include e.g. measures like r-squared, intraclass correlation
    coefficient (Nakagawa, Johnson & Schielzeth (2017)
    <doi:10.1098/rsif.2017.0213>), root mean squared error or functions to
    check models for overdispersion, singularity or zero-inflation and
    more. Functions apply to a large variety of regression models,
    including generalized linear models, mixed effects models and Bayesian
    models. References: Lüdecke et al. (2021) <doi:10.21105/joss.03139>.
	"""
	
	homepage = "https://easystats.github.io/performance/"
	cran = "performance" 

	version("0.10.9", md5="07a07184ab81c70c92646ab990e0fd5f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.2:", type=("build", "run"))
	depends_on("r-insight@0.19.8:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
