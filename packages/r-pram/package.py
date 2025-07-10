# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPram(RPackage):
	"""Pooling RNA-seq datasets for assembling transcript models

	Publicly available RNA-seq data is routinely used for retrospective analysis to elucidate new biology.  Novel transcript discovery enabled by large collections of RNA-seq datasets has emerged as one of such analysis.  To increase the power of transcript discovery from large collections of RNA-seq datasets, we developed a new R package named Pooling RNA-seq and Assembling Models (PRAM), which builds transcript models in intergenic regions from pooled RNA-seq datasets.  This package includes functions for defining intergenic regions, extracting and pooling related RNA-seq alignments, predicting, selected, and evaluating transcript models.
	"""
	
	homepage = "https://github.com/pliu55/pram"
	bioc = "pram" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pram_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pram/pram_1.18.0.tar.gz"]

	version("1.18.0", sha256="9dec0d2b7955d55267ec80c39f83c965cb392993e917de11330a9b15540e2dfe")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-genomicalignments@1.16:", type=("build", "run"))
	depends_on("r-rtracklayer@1.40.6:", type=("build", "run"))
	depends_on("r-biocgenerics@0.26:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.16:", type=("build", "run"))
	depends_on("r-genomicranges@1.32:", type=("build", "run"))
	depends_on("r-iranges@2.14.12:", type=("build", "run"))
	depends_on("r-rsamtools@1.32.3:", type=("build", "run"))
	depends_on("r-s4vectors@0.18.3:", type=("build", "run"))
