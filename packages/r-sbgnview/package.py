# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbgnview(RPackage):
	""""SBGNview: Data Analysis, Integration and Visualization on SBGN Pathways"

	SBGNview is a tool set for pathway based data visalization, integration and analysis. SBGNview is similar and complementary to the widely used Pathview, with the following key features: 1. Pathway definition by the widely adopted Systems Biology Graphical Notation (SBGN); 2. Supports multiple major pathway databases beyond KEGG (Reactome, MetaCyc, SMPDB, PANTHER, METACROP) and user defined pathways; 3. Covers 5,200 reference pathways and over 3,000 species by default; 4. Extensive graphics controls, including glyph and edge attributes, graph layout and sub-pathway highlight; 5. SBGN pathway data manipulation, processing, extraction and analysis.
	"""
	
	homepage = "https://github.com/datapplab/SBGNview"
	bioc = "SBGNview" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SBGNview_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SBGNview/SBGNview_1.16.0.tar.gz"]

	version("1.16.0", md5="785b51f08ce7b40f23b6e9168ce1d1af")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pathview", type=("build", "run"))
	depends_on("r-sbgnview-data", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
