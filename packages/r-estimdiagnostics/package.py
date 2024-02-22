# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimdiagnostics(RPackage):
	"""Diagnostic Tools and Unit Tests for Statistical Estimators

	Extension of 'testthat' package to make unit tests on empirical distributions of estimators and functions for diagnostics of their finite-sample performance.
	"""
	
	homepage = "https://gitlab.com/Dmitry_Otryakhin/diagnostics-and-tests-for-statistical-estimators"
	cran = "EstimDiagnostics" 

	version("0.0.3", md5="916a0973e3cb0ec01c870aa9147ad558")

	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-goftest@1.2.2:", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
