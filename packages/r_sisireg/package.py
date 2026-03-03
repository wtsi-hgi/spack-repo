# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSisireg(RPackage):
	"""Sign-Simplicity-Regression-Solver

	Implementation of the SSR-Algorithm. The Sign-Simplicity-Regression model is a nonparametric statistical model which is based on residual signs and simplicity assumptions on the regression function. Goal is to calculate the most parsimonious regression function satisfying the statistical adequacy requirements. Theory and functions are specified in Metzner (2020, ISBN: 979-8-68239-420-3, "Trendbasierte Prognostik") and Metzner (2021, ISBN: 979-8-59347-027-0, "Adäquates Maschinelles Lernen").
	"""
	
	cran = "sisireg" 

	version("1.1.1", md5="9f912f1823daf87bcdc01b21516dc270")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
