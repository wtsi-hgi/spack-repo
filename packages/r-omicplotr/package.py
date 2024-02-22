# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicplotr(RPackage):
	"""Visual Exploration of Omic Datasets Using a Shiny App

	A Shiny app for visual exploration of omic datasets as compositions, and differential abundance analysis using ALDEx2. Useful for exploring RNA-seq, meta-RNA-seq, 16s rRNA gene sequencing with visualizations such as principal component analysis biplots (coloured using metadata for visualizing each variable), dendrograms and stacked bar plots, and effect plots (ALDEx2). Input is a table of counts and metadata file (if metadata exists), with options to filter data by count or by metadata to remove low counts, or to visualize select samples according to selected metadata.
	"""
	
	bioc = "omicplotR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/omicplotR_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/omicplotR/omicplotR_1.22.0.tar.gz"]

	version("1.22.0", md5="1ab1c2e82c98f8086b4dba4f65a613e7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-aldex2@1.18:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-zcompositions", type=("build", "run"))
