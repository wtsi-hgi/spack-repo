# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffcyt(RPackage):
	"""Differential discovery in high-dimensional cytometry via high-resolution clustering

	Statistical methods for differential discovery analyses in high-dimensional cytometry data (including flow cytometry, mass cytometry or CyTOF, and oligonucleotide-tagged cytometry), based on a combination of high-resolution clustering and empirical Bayes moderated tests adapted from transcriptomics.
	"""
	
	homepage = "https://github.com/lmweber/diffcyt"
	bioc = "diffcyt" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/diffcyt_1.22.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/diffcyt/diffcyt_1.22.1.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.1", sha256="f2a22afb63dd4512533238e411a3d1f4cdc7c9afcd1f5bc22ae3da56c760e7d1")
	version("1.22.0", md5="8118267e493c2646533a9730a876d340")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowsom", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
