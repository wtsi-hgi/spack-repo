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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MSstatsQC_2.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MSstatsQC/MSstatsQC_2.20.0.tar.gz"]

    version("2.26.0", tag="RELEASE_3_21")
	version("2.20.0", sha256="82d854fc7eb8f84e16b372cffe8fb50c05e0c540705f4b0b08553ab28917c151")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-qcmetrics", type=("build", "run"))
