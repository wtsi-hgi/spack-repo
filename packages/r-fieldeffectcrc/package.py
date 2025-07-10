# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFieldeffectcrc(RPackage):
	"""Tumor, tumor-adjacent normal, and healthy colorectal transcriptomes as SummarizedExperiment objects

	Processed RNA-seq data for 1,139 human primary colorectal tissue samples across three phenotypes, including tumor, normal adjacent-to-tumor, and healthy, available as Synapse ID syn22237139 on synapse.org. Data have been parsed into SummarizedExperiment objects available via ExperimentHub to facilitate reproducibility and extension of results from Dampier et al. (PMCID: PMC7386360, PMID: 32764205).
	"""
	
	homepage = "http://bioconductor.org/packages/release/bioc/html/FieldEffectCrc.html"
	bioc = "FieldEffectCrc" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FieldEffectCrc_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FieldEffectCrc/FieldEffectCrc_1.12.0.tar.gz"]

	version("1.12.0", sha256="46ddc3ac201ad37bceb86af48ad9036d9e77f359855867fd1cabec92f2f5bf8f")

	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub@0.99.6:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))

