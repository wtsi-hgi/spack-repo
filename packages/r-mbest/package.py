# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbest(RPackage):
	"""Moment-Based Estimation for Hierarchical Models

	Fast moment-based hierarchical model fitting. Implements
    methods from the papers
    "Fast Moment-Based Estimation for Hierarchical Models," by Perry (2017)
    and
    "Fitting a Deeply Nested Hierarchical Model to a Large Book Review
    Dataset Using a Moment-Based Estimator," by Zhang, Schmaus, and Perry
    (2018).
	"""
	
	homepage = "https://github.com/patperry/r-mbest"
	cran = "mbest" 

	version("0.6", md5="c2e6a2a3622e9434e42d2f62641f8641")

	depends_on("r-nlme@3.1.124:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
