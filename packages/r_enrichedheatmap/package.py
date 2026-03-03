# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichedheatmap(RPackage):
	"""Making Enriched Heatmaps

	Enriched heatmap is a special type of heatmap which visualizes the enrichment of genomic signals on specific target regions. Here we implement enriched heatmap by ComplexHeatmap package. Since this type of heatmap is just a normal heatmap but with some special settings, with the functionality of ComplexHeatmap, it would be much easier to customize the heatmap as well as concatenating to a list of heatmaps to show correspondance between different data sources.
	"""
	
	homepage = "https://github.com/jokergoo/EnrichedHeatmap"
	bioc = "EnrichedHeatmap" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EnrichedHeatmap_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EnrichedHeatmap/EnrichedHeatmap_1.32.0.tar.gz"]

	version("1.32.0", md5="269aeb6d749072508069805663216dc4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-complexheatmap@2.11:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-circlize@0.4.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
