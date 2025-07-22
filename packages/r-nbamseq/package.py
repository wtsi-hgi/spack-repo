# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbamseq(RPackage):
	"""Negative Binomial Additive Model for RNA-Seq Data

	High-throughput sequencing experiments followed by differential expression analysis is a widely used approach to detect genomic biomarkers. A fundamental step in differential expression analysis is to model the association between gene counts and covariates of interest. NBAMSeq a flexible statistical model based on the generalized additive model and allows for information sharing across genes in variance estimation.
	"""
	
	homepage = "https://github.com/reese3928/NBAMSeq"
	bioc = "NBAMSeq"

	version("1.24.1", commit="4cf2748c1831d7a4d9e863db2aa5ed738645e717")
	version("1.18.0", commit="56721c1c7b49de56844d5049d1de2d4f36ad7bd5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-mgcv@1.8.24:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
