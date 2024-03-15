# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeconrnaseq(RPackage):
	"""Deconvolution of Heterogeneous Tissue Samples for mRNA-Seq data

	DeconSeq is an R package for deconvolution of heterogeneous tissues based on mRNA-Seq data. It modeled expression levels from heterogeneous cell populations in mRNA-Seq as the weighted average of expression from different constituting cell types and predicted cell type proportions of single expression profiles.
	"""
	
	bioc = "DeconRNASeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DeconRNASeq_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DeconRNASeq/DeconRNASeq_1.44.0.tar.gz"]

	version("1.44.0", md5="d38af67b8408b66b85fbb4061442b953")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
