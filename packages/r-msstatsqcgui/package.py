# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsqcgui(RPackage):
	"""A graphical user interface for MSstatsQC package

	MSstatsQCgui is a Shiny app which provides longitudinal system suitability monitoring and quality control tools for proteomic experiments.
	"""
	
	homepage = "http://msstats.org/msstatsqc"
	bioc = "MSstatsQCgui" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MSstatsQCgui_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MSstatsQCgui/MSstatsQCgui_1.22.0.tar.gz"]

	version("1.22.0", sha256="d7f34387d63f2d65c608310caf704b739e2436dcfcbb03517c801b6d6769740c")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-msstatsqc", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
