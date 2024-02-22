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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dcanr_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dcanr/dcanr_1.18.0.tar.gz"]

	version("1.18.0", md5="1a30832879c85ae9430a463d581ba978")

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
