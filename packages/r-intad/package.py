# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntad(RPackage):
	"""Search for correlation between epigenetic signals and gene expression in TADs

	The package is focused on the detection of correlation between expressed genes and selected epigenomic signals (i.e. enhancers obtained from ChIP-seq data) either within topologically associated domains (TADs) or between chromatin contact loop anchors. Various parameters can be controlled to investigate the influence of external factors and visualization plots are available for each analysis step.
	"""
	
	bioc = "InTAD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/InTAD_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/InTAD/InTAD_1.22.0.tar.gz"]

	version("1.22.0", sha256="56c466237ea97cc3c44cad80e97dc00dfcff23707ea235357fd4bdc7ccde7c07")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
