# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcanr(RPackage):
	"""Differential co-expression/association network analysis

	This package implements methods and an evaluation framework to infer differential co-expression/association networks. Various methods are implemented and can be evaluated using simulated datasets. Inference of differential co-expression networks can allow identification of networks that are altered between two conditions (e.g., health and disease).
	"""
	
	homepage = "https://davislaboratory.github.io/dcanr/"
	bioc = "dcanr"

	version("1.24.0", commit="d2ed25798817e22bce98c23d211b570d9f65e553")
	version("1.18.0", commit="01a78db95b5b5b0a695721d78b296e4781953604")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
