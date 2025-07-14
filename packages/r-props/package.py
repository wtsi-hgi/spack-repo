# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProps(RPackage):
	"""PRObabilistic Pathway Score (PROPS)

	This package calculates probabilistic pathway scores using gene expression data. Gene expression values are aggregated into pathway-based scores using Bayesian network representations of biological pathways.
	"""
	
	bioc = "PROPS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PROPS_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PROPS/PROPS_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="e3a480e8867843c33c84a8d21ffe84ae6d27ebbaf12db4278326d4edf57082cd")

	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
