# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrmetrics(RPackage):
	"""Calculate growth-rate inhibition (GR) metrics

	Functions for calculating and visualizing growth-rate inhibition (GR) metrics.
	"""
	
	homepage = "https://github.com/uc-bd2k/GRmetrics"
	bioc = "GRmetrics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GRmetrics_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GRmetrics/GRmetrics_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="2936848c2fe210ba6ce82cddcd7f7462e1bd0336150283066cda108a265fbc64")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
