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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rbec_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rbec/Rbec_1.10.0.tar.gz"]

	version("1.10.0", md5="f295d8ade5faf2c0b770f2b075262116")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dada2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
