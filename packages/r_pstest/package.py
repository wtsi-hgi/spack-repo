# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPstest(RPackage):
	"""Specification Tests for Parametric Propensity Score Models

	The propensity score is one of the most widely used tools in
    studying the causal effect of a treatment, intervention, or policy. Given that
    the propensity score is usually unknown, it has to be estimated, implying that
    the reliability of many treatment effect estimators depends on the correct
    specification of the (parametric) propensity score. This package implements the
    data-driven nonparametric diagnostic tools for detecting propensity score
    misspecification proposed by Sant'Anna and Song (2019) <doi:10.1016/j.jeconom.2019.02.002>.
	"""
	
	homepage = "https://github.com/pedrohcgs/pstest"
	cran = "pstest" 

	version("0.1.3.900", md5="cb3f69caa329ab6e7a7ed89365f3f237")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-glmx", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
