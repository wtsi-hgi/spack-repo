# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValmetrics(RPackage):
	"""Metrics and Plots for Model Evaluation

	Functions for metrics and plots for model evaluation. Based on vectors of observed and predicted values. Method: Kristin Piikki, Johanna Wetterlind, Mats Soderstrom and Bo Stenberg (2021). <doi:10.1111/SUM.12694>. 
	"""
	
	cran = "valmetrics" 

	version("1.0.0", md5="4f3cd99d5f5f650eb58fbe12a41673a0")

	depends_on("r@4:", type=("build", "run"))
