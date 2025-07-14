# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBusseq(RPackage):
	"""Batch Effect Correction with Unknow Subtypes for scRNA-seq data

	BUSseq R package fits an interpretable Bayesian hierarchical model---the Batch Effects Correction with Unknown Subtypes for scRNA seq Data (BUSseq)---to correct batch effects in the presence of unknown cell types. BUSseq is able to simultaneously correct batch effects, clusters cell types, and takes care of the count data nature, the overdispersion, the dropout events, and the cell-specific sequencing depth of scRNA-seq data. After correcting the batch effects with BUSseq, the corrected value can be used for downstream analysis as if all cells were sequenced in a single batch. BUSseq can integrate read count matrices obtained from different scRNA-seq platforms and allow cell types to be measured in some but not all of the batches as long as the experimental design fulfills the conditions listed in our manuscript.
	"""
	
	homepage = "https://github.com/songfd2018/BUSseq"
	bioc = "BUSseq"

	version("1.14.0", commit="48ad5e0305a2c1344bf27aee83cc35f17b013c22")
	version("1.8.0", commit="c8be50e324981bc7f407bf691fd197a8ff763461")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
