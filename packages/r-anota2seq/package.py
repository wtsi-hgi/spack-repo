# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnota2seq(RPackage):
	"""Generally applicable transcriptome-wide analysis of translational efficiency using anota2seq

	anota2seq provides analysis of translational efficiency and differential expression analysis for polysome-profiling and ribosome-profiling studies (two or more sample classes) quantified by RNA sequencing or DNA-microarray. Polysome-profiling and ribosome-profiling typically generate data for two RNA sources; translated mRNA and total mRNA. Analysis of differential expression is used to estimate changes within each RNA source (i.e. translated mRNA or total mRNA). Analysis of translational efficiency aims to identify changes in translation efficiency leading to altered protein levels that are independent of total mRNA levels (i.e. changes in translated mRNA that are independent of levels of total mRNA) or buffering, a mechanism regulating translational efficiency so that protein levels remain constant despite fluctuating total mRNA levels (i.e. changes in total mRNA that are independent of levels of translated mRNA). anota2seq applies analysis of partial variance and the random variance model to fulfill these tasks.
	"""
	
	bioc = "anota2seq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/anota2seq_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/anota2seq/anota2seq_1.24.0.tar.gz"]

	version("1.24.0", sha256="562a98a6175eff25a4ff39493f35eeea0c38f44ccbc1d1c726bfe05d24e4dd4f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
