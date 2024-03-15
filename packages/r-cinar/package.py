# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCinar(RPackage):
	"""A Computational Pipeline for Bulk 'ATAC-Seq' Profiles

	Differential analyses and Enrichment pipeline for bulk 'ATAC-seq' data
  analyses. This package combines different packages to have an ultimate package
  for both data analyses and visualization of 'ATAC-seq' data. Methods are described in 
  'Karakaslar et al.' (2021) <doi:10.1101/2021.03.05.434143>.
	"""
	
	homepage = "https://github.com/eonurk/cinaR/"
	cran = "cinaR" 

	version("0.2.3", md5="4c8ef0c2f3271633e69b8e72e70d5e5c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm10-knowngene", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
