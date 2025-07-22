# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaagecalc(RPackage):
	"""A multi-tissue transcriptional age calculator

	It has been shown that both DNA methylation and RNA transcription are linked to chronological age and age related diseases. Several estimators have been developed to predict human aging from DNA level and RNA level. Most of the human transcriptional age predictor are based on microarray data and limited to only a few tissues. To date, transcriptional studies on aging using RNASeq data from different human tissues is limited. The aim of this package is to provide a tool for across-tissue and tissue-specific transcriptional age calculation based on GTEx RNASeq data.
	"""
	
	homepage = "https://github.com/reese3928/RNAAgeCalc"
	bioc = "RNAAgeCalc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAAgeCalc_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAAgeCalc/RNAAgeCalc_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="72ca209df31c620727903c7538cd7215ca4070550d413e5a604f03e6bb2328b3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-recount", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
