# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignifinder(RPackage):
	"""Implementations of transcriptional cancer signatures

	signifinder is an R package for computing and exploring a compendium of tumor signatures. It allows to compute a variety of signatures, based on gene expression values, and return single-sample scores. Currently, signifinder contains 46 distinct signatures collected from the literature, relating to multiple tumors and multiple cancer processes.
	"""
	
	homepage = "https://github.com/CaluraLab/signifinder"
	bioc = "signifinder" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/signifinder_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/signifinder/signifinder_1.4.0.tar.gz"]

	version("1.4.0", md5="f24a46dbbbc9b688450e9f2a0e2e221e")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dgeobj-utils", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-consensusov", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-maxstat", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
