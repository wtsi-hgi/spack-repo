# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTripr(RPackage):
	"""T-cell Receptor/Immunoglobulin Profiler (TRIP)

	TRIP is a software framework that provides analytics services on antigen receptor (B cell receptor immunoglobulin, BcR IG | T cell receptor, TR) gene sequence data. It is a web application written in R Shiny. It takes as input the output files of the IMGT/HighV-Quest tool. Users can select to analyze the data from each of the input samples separately, or the combined data files from all samples and visualize the results accordingly.
	"""
	
	homepage = "https://github.com/BiodataAnalysisGroup/tripr"
	bioc = "tripr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tripr_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tripr/tripr_1.8.0.tar.gz"]

	version("1.8.0", sha256="f626700f1d8eef5d1d53fb33b59bc91d166fa45515ac5b384d479bce61edc721")

	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-golem@0.3.1:", type=("build", "run"))
