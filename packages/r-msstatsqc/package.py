# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsqc(RPackage):
	"""Longitudinal system suitability monitoring and quality control for proteomic experiments

	MSstatsQC is an R package which provides longitudinal system suitability monitoring and quality control tools for proteomic experiments.
	"""
	
	homepage = "http://msstats.org/msstatsqc"
	bioc = "MSstatsQC"

	version("2.26.0", commit="f36559bf9c78b5c3174f257857c50fc3546803e7")
	version("2.20.0", commit="970a773be096d99852e41545dfde14a020ec2dff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-qcmetrics", type=("build", "run"))
