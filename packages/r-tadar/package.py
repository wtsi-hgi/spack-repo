# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTadar(RPackage):
	"""Transcriptome Analysis of Differential Allelic Representation

	This package provides functions to standardise the analysis of Differential Allelic Representation (DAR). DAR compromises the integrity of Differential Expression analysis results as it can bias expression, influencing the classification of genes (or transcripts) as being differentially expressed. DAR analysis results in an easy-to-interpret value between 0 and 1 for each genetic feature of interest, where 0 represents identical allelic representation and 1 represents complete diversity. This metric can be used to identify features prone to false-positive calls in Differential Expression analysis, and can be leveraged with statistical methods to alleviate the impact of such artefacts on RNA-seq data.
	"""
	
	homepage = "https://github.com/baerlachlan/tadar"
	bioc = "tadar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tadar_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tadar/tadar_1.0.0.tar.gz"]

	version("1.0.0", sha256="e5ca296ed8db6cae9aa93322f2b3f77fac41c0caa56ec90efe540011077f69ec")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
