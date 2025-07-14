# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIhwpaper(RPackage):
	"""Reproduce figures in IHW paper

	This package conveniently wraps all functions needed to reproduce the figures in the IHW paper (https://www.nature.com/articles/nmeth.3885) and the data analysis in https://rss.onlinelibrary.wiley.com/doi/10.1111/rssb.12411, cf. the arXiv preprint (http://arxiv.org/abs/1701.05179). Thus it is a companion package to the Bioconductor IHW package.
	"""
	
	bioc = "IHWpaper" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/IHWpaper_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/IHWpaper/IHWpaper_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="b2e6d8674910ccf6b7406ae1ad88effb62430e6a6f348a3b61128328b0650b1b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ihw", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))

