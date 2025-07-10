# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProgeny(RPackage):
	"""Pathway RespOnsive GENes for activity inference from gene expression

	PROGENy is resource that leverages a large compendium of publicly available signaling perturbation experiments to yield a common core of pathway responsive genes for human and mouse. These, coupled with any statistical method, can be used to infer pathway activities from bulk or single-cell transcriptomics.
	"""
	
	homepage = "https://github.com/saezlab/progeny"
	bioc = "progeny" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/progeny_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/progeny/progeny_1.24.0.tar.gz"]

	version("1.24.0", sha256="14b3f8e2ff46459f5c5bccc962edd38e2068b1fbff62878881ebf4ea44e48fde")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-decoupler", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
