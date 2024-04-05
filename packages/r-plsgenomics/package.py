# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsgenomics(RPackage):
	"""PLS Analyses for Genomics

	Routines for PLS-based genomic analyses,
        implementing PLS methods for classification with
        microarray data and prediction of transcription factor
        activities from combined ChIP-chip analysis. The >=1.2-1
        versions include two new classification methods for microarray
        data: GSIM and Ridge PLS. The >=1.3 versions includes a
        new classification method combining variable selection and
        compression in logistic regression context: logit-SPLS; and
        an adaptive version of the sparse PLS.
	"""
	
	homepage = "https://github.com/gdurif/plsgenomics"
	cran = "plsgenomics" 

	version("1.5-3", md5="1b59eed464388dcc9c95a06e901ee77b")
	version("1.5-2.1", md5="7b18723db35f52352a36f16d19b5724e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
