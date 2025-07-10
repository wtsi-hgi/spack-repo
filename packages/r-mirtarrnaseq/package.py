# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirtarrnaseq(RPackage):
	"""mirTarRnaSeq

	mirTarRnaSeq R package can be used for interactive mRNA miRNA sequencing statistical analysis. This package utilizes expression or differential expression mRNA and miRNA sequencing results and performs interactive correlation and various GLMs (Regular GLM, Multivariate GLM, and Interaction GLMs ) analysis between mRNA and miRNA expriments. These experiments can be time point experiments, and or condition expriments.
	"""
	
	bioc = "mirTarRnaSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mirTarRnaSeq_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mirTarRnaSeq/mirTarRnaSeq_1.10.0.tar.gz"]

	version("1.10.0", sha256="947b4a660e6c01424e033bd22a2dcbd60cce916f4e1726beacdb2664ee0edd51")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
