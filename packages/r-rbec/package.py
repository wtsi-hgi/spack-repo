# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbec(RPackage):
	"""Rbec: a tool for analysis of amplicon sequencing data from synthetic microbial communities

	Rbec is a adapted version of DADA2 for analyzing amplicon sequencing data from synthetic communities (SynComs), where the reference sequences for each strain exists. Rbec can not only accurately profile the microbial compositions in SynComs, but also predict the contaminants in SynCom samples.
	"""
	
	bioc = "Rbec"

	version("1.16.0", commit="1cdfeb49ba1a761b26888b69ef68f8ed847ef1e0")
	version("1.10.0", commit="fa01a45bd8d1827000de7268fbccb1716974c032")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dada2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
