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

	version("1.50.0", commit="20915cdb7bbb4070959db2a1ce7ef6e6c1fbfdce")
	version("1.44.0", commit="b74d94cfb15a475cad1ef919a2f37a21985f66ab")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
