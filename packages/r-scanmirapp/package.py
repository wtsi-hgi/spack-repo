# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanmirapp(RPackage):
	"""scanMiR shiny application

	A shiny interface to the scanMiR package. The application enables the scanning of transcripts and custom sequences for miRNA binding sites, the visualization of KdModels and binding results, as well as browsing predicted repression data. In addition contains the IndexedFst class for fast indexed reading of large GenomicRanges or data.frames, and some utilities for facilitating scans and identifying enriched miRNA-target pairs.
	"""
	
	bioc = "scanMiRApp" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scanMiRApp_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scanMiRApp/scanMiRApp_1.8.0.tar.gz"]

	version("1.8.0", md5="637ec69edde646093548d190325738fe")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scanmir", type=("build", "run"))
	depends_on("r-scanmirdata", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
