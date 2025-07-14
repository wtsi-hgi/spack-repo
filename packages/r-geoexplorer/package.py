# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoexplorer(RPackage):
	"""GEOexplorer: a webserver for gene expression analysis and visualisation

	GEOexplorer is a webserver and R/Bioconductor package and web application that enables users to perform gene expression analysis. The development of GEOexplorer was made possible because of the excellent code provided by GEO2R (https: //www.ncbi.nlm.nih.gov/geo/geo2r/).
	"""
	
	homepage = "https://github.com/guypwhunt/GEOexplorer/"
	bioc = "GEOexplorer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GEOexplorer_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GEOexplorer/GEOexplorer_1.8.0.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="fce2f86eb58a9ba5892e33f9d4c31d6b05a129c16096e2ba021d8ab6b0d412ca")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-enrichr", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinyheatmaply", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
