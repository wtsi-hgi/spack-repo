# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBraidreports(RPackage):
	"""Visualize Combined Action Response Surfaces and Report BRAID
Analyses

	Provides functions to generate, format, and style surface plots for visualizing combined action data.  Also provides functions for reporting on a BRAID analysis, including plotting curve-shifts, calculating IAE values, and producing full BRAID analysis reports.
	"""
	
	cran = "braidReports" 

	version("0.5.4", md5="96f2e432ddc142faff05f99b55f19049")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-braidrm", type=("build", "run"))
