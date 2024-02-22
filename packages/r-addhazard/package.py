# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddhazard(RPackage):
	"""Fit Additive Hazards Models for Survival Analysis

	Contains tools to fit the additive hazards model to data from a cohort,
    random sampling, two-phase Bernoulli sampling and two-phase finite population sampling,
    as well as calibration tool to incorporate phase I auxiliary information into the
    two-phase data model fitting.  This package provides regression parameter estimates and
    their model-based and robust standard errors. It also offers tools to make prediction of
    individual specific hazards.
	"""
	
	cran = "addhazard" 

	version("1.1.0", md5="d1807f625f1b0c4cd3866a20087b2a33")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-ahaz", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
