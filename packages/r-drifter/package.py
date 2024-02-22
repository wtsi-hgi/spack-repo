# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrifter(RPackage):
	"""Concept Drift and Concept Shift Detection for Predictive Models

	Concept drift refers to the change in the data distribution or 
  in the relationships between variables over time.
  'drifter' calculates distances between variable distributions or 
  variable relations and identifies both types of drift. 
  Key functions are: 
  calculate_covariate_drift() checks distance between corresponding variables in two datasets,
  calculate_residuals_drift() checks distance between residual distributions for two models,
  calculate_model_drift() checks distance between partial dependency profiles for two models,
  check_drift() executes all checks against drift.
  'drifter' is a part of the 'DrWhy.AI' universe (Biecek 2018) <arXiv:1806.08915>.
	"""
	
	homepage = "https://ModelOriented.github.io/drifter/"
	cran = "drifter" 

	version("0.2.1", md5="285f8fe796dc0aaa8fe65296e925183b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ingredients", type=("build", "run"))
