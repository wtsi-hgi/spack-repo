# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcobra(RPackage):
	"""Comparison and Visualization of Ranking and Assignment Methods

	This package provides functions for calculation and visualization of performance metrics for evaluation of ranking and binary classification (assignment) methods. Various types of performance plots can be generated programmatically. The package also contains a shiny application for interactive exploration of results.
	"""
	
	homepage = "https://github.com/csoneson/iCOBRA"
	bioc = "iCOBRA"

	version("1.36.0", commit="1be9ea5db5afb2fbae93b290e1e5371ea7a3dc3a")
	version("1.30.0", commit="e89626692bc0409ec98db32722c1a58c7e50b6c4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@0.9.1.9008:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
