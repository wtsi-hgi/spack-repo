# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnowseq(RPackage):
	"""KnowSeq R/Bioc package: The Smart Transcriptomic Pipeline

	KnowSeq proposes a novel methodology that comprises the most relevant steps in the Transcriptomic gene expression analysis. KnowSeq expects to serve as an integrative tool that allows to process and extract relevant biomarkers, as well as to assess them through a Machine Learning approaches. Finally, the last objective of KnowSeq is the biological knowledge extraction from the biomarkers (Gene Ontology enrichment, Pathway listing and Visualization and Evidences related to the addressed disease). Although the package allows analyzing all the data manually, the main strenght of KnowSeq is the possibilty of carrying out an automatic and intelligent HTML report that collect all the involved steps in one document. It is important to highligh that the pipeline is totally modular and flexible, hence it can be started from whichever of the different steps. KnowSeq expects to serve as a novel tool to help to the experts in the field to acquire robust knowledge and conclusions for the data and diseases to study.
	"""
	
	bioc = "KnowSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/KnowSeq_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/KnowSeq/KnowSeq_1.16.0.tar.gz"]

	version("1.16.0", md5="b57c9661e3de8e27e79e3809a609acda")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cqn@1.28.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-praznik", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sva@3.30.1:", type=("build", "run"))
	depends_on("r-edger@3.24.3:", type=("build", "run"))
	depends_on("r-limma@3.38.3:", type=("build", "run"))
	depends_on("r-hmisc@4.4:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
