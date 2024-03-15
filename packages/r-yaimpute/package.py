# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYaimpute(RPackage):
	"""Nearest Neighbor Observation Imputation and Evaluation Tools.

	Performs nearest neighbor-based imputation using one or more alternative
	approaches to processing multivariate data. These include methods based on
	canonical correlation analysis, canonical correspondence analysis, and a
	multivariate adaptation of the random forest classification and regression
	techniques of Leo Breiman and Adele Cutler. Additional methods are also
	offered. The package includes functions for comparing the results from
	running alternative techniques, detecting imputation targets that are
	notably distant from reference observations, detecting and correcting for
	bias, bootstrapping and building ensemble imputations, and mapping
	results."""

	cran = "yaImpute"

	version("1.0-34", md5="d4e6899077278d5386b0063a2d4be696")

	depends_on("r@3:", type=("build", "run"))
