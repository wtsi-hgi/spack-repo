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

    version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="6f8f7237e2acbe2e5b2248da61484ed289efb1769eab2fb793e0257e52cfbdcc")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
