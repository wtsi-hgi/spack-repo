# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohcap(RPackage):
	"""CpG Island Analysis Pipeline for Illumina Methylation Array and Targeted BS-Seq Data

	COHCAP (pronounced "co-cap") provides a pipeline to analyze single-nucleotide resolution methylation data (Illumina 450k/EPIC methylation array, targeted BS-Seq, etc.). It provides differential methylation for CpG Sites, differential methylation for CpG Islands, integration with gene expression data, with visualizaton options. Discussion Group: https://sourceforge.net/p/cohcap/discussion/bioconductor/
	"""
	
	bioc = "COHCAP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/COHCAP_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/COHCAP/COHCAP_1.48.0.tar.gz"]

	version("1.48.0", sha256="cdde22c9ed7ff8e2a433e1f8b917194fbedeb112a4c42b1cefe4369aabacebb3")

	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-cohcapanno", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
