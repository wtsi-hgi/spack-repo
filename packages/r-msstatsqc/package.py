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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSstatsQC_2.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSstatsQC/MSstatsQC_2.20.0.tar.gz"]

	version("2.20.0", md5="9328babd37ae774a13dff37e38088339")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-qcmetrics", type=("build", "run"))
