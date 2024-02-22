# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgsa(RPackage):
	"""Time-Course Gene Set Analysis

	Implementation of Time-course Gene Set Analysis (TcGSA), a method for 
	analyzing longitudinal gene-expression data at the gene set level. Method is
	detailed in: Hejblum, Skinner & Thiebaut (2015) <doi: 10.1371/journal.pcbi.1004310>.
	"""
	
	homepage = "http://sistm.github.io/TcGSA/"
	cran = "TcGSA" 

	version("0.12.10", md5="a56d343e230fa705e0d64181e166b8c4")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-lme4@1.0.4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gsa", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
