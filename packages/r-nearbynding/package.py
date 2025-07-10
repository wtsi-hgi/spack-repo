# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNearbynding(RPackage):
	"""Discern RNA structure proximal to protein binding

	Provides a pipeline to discern RNA structure at and proximal to the site of protein binding within regions of the transcriptome defined by the user. CLIP protein-binding data can be input as either aligned BAM or peak-called bedGraph files. RNA structure can either be predicted internally from sequence or users have the option to input their own RNA structure data. RNA structure binding profiles can be visually and quantitatively compared across multiple formats.
	"""
	
	bioc = "nearBynding" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nearBynding_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nearBynding/nearBynding_1.12.0.tar.gz"]

	version("1.12.0", sha256="bf7cc77fbb04178e251994f5a8dfb985457b4571802b7be7026bc9a2ac529a84")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("bedtools2@2.28.0:", type=("build", "link", "run"))
