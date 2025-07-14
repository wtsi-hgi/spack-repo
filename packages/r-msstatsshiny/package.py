# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsshiny(RPackage):
	"""MSstats GUI for Statistical Anaylsis of Proteomics Experiments

	MSstatsShiny is an R-Shiny graphical user interface (GUI) integrated with the R packages MSstats, MSstatsTMT, and MSstatsPTM. It provides a point and click end-to-end analysis pipeline applicable to a wide variety of experimental designs. These include data-dependedent acquisitions (DDA) which are label-free or tandem mass tag (TMT)-based, as well as DIA, SRM, and PRM acquisitions and those targeting post-translational modifications (PTMs). The application automatically saves users selections and builds an R script that recreates their analysis, supporting reproducible data analysis.
	"""
	
	bioc = "MSstatsShiny" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MSstatsShiny_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MSstatsShiny/MSstatsShiny_1.4.3.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.3", sha256="e3f9833bff4318bcedc6e027819bd72d611db84e62eab68c2dc79ec6222aea71")
	version("1.4.2", md5="2a58cf6ab9674a13b96e66974d6b15a0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
	depends_on("r-msstatstmt", type=("build", "run"))
	depends_on("r-msstatsptm", type=("build", "run"))
	depends_on("r-msstatsconvert", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mockery", type=("build", "run"))
