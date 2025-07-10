# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlseq(RPackage):
	"""RLSeq: An analysis package for R-loop mapping data

	RLSeq is a toolkit for analyzing and evaluating R-loop mapping datasets. RLSeq serves two primary purposes: (1) to facilitate the evaluation of dataset quality, and (2) to enable R-loop analysis in the context of publicly-available data sets from RLBase. The package is intended to provide a simple pipeline, called with the `RLSeq()` function, which performs all main analyses. Individual functions are also accessible and provide custom analysis capabilities. Finally an HTML report is generated with `report()`.
	"""
	
	homepage = "https://github.com/Bishop-Laboratory/RLSeq"
	bioc = "RLSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RLSeq_1.5.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RLSeq/RLSeq_1.5.2.tar.gz"]

	version("1.5.2", sha256="38e8d3f29c7c6a3a29d1ddb49a1674073a0beb9a7844de38bc66af17c4b8115a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-valr", type=("build", "run"))
	depends_on("r-caretensemble", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-ggprism", type=("build", "run"))
	depends_on("r-rlhub", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
