# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGladiatox(RPackage):
	"""R Package for Processing High Content Screening data

	GladiaTOX R package is an open-source, flexible solution to high-content screening data processing and reporting in biomedical research. GladiaTOX takes advantage of the tcpl core functionalities and provides a number of extensions: it provides a web-service solution to fetch raw data; it computes severity scores and exports ToxPi formatted files; furthermore it contains a suite of functionalities to generate pdf reports for quality control and data processing.
	"""
	
	bioc = "GladiaTOX" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GladiaTOX_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GladiaTOX/GladiaTOX_1.18.0.tar.gz"]

	version("1.18.0", sha256="564c1662530f9d677157ee093bf81768e01f18550a49e7448fa9c44b64100b06")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmariadb", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
