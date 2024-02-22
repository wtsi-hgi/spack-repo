# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerry(RPackage):
	"""Resampling-Based Prediction Error Estimation for Regression
Models

	Tools that allow developers to write functions for prediction
    error estimation with minimal programming effort and assist users with
    model selection in regression problems.
	"""
	
	cran = "perry" 

	version("0.3.1", md5="3a115117c8d545fb048e211a025ab63f")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
