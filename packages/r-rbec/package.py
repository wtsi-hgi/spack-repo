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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rbec_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rbec/Rbec_1.10.0.tar.gz"]

	version("1.10.0", sha256="c364ed6bca9c1117ac3ce10da92bd907ced22234a77c39420dd5c8e2c11e51c2")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dada2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
