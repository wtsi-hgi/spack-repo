# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetategarch(RPackage):
	"""Simulation, Estimation and Forecasting of Beta-Skew-t-EGARCH
Models

	Simulation, estimation and forecasting of first-order Beta-Skew-t-EGARCH models with leverage (one-component, two-component, skewed versions).
	"""
	
	homepage = "http://www.sucarrat.net/"
	cran = "betategarch" 

	version("3.3", md5="1c6ac5ae57670b8a5109c018d7f0a16b")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
