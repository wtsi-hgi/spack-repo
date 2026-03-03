# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeva(RPackage):
	"""Model Evaluation and Analysis

	Analyses species distribution models and evaluates their performance. It includes functions for variation partitioning, extracting variable importance, computing several metrics of model discrimination and calibration performance, optimizing prediction thresholds based on a number of criteria, performing multivariate environmental similarity surface (MESS) analysis, and displaying various analytical plots. Initially described in Barbosa et al. (2013) <doi:10.1111/ddi.12100>.
	"""
	
	homepage = "http://modeva.r-forge.r-project.org/"
	cran = "modEvA" 

	version("3.13.3", md5="1d758d83cc6fdfe99132d507e2d64d78")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-terra@1.5.50:", type=("build", "run"))
