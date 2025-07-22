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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NBAMSeq_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NBAMSeq/NBAMSeq_1.18.0.tar.gz"]

	version("1.24.1", tag="RELEASE_3_21")
	version("1.18.0", sha256="597142f74149e45735a3508b8ea0e2019715a09b2156d768c0c904522f1c5357")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-mgcv@1.8.24:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
