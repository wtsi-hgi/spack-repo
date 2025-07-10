# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGosim(RPackage):
	"""Computation of functional similarities between GO terms and gene products; GO enrichment analysis

	This package implements several functions useful for computing similarities between GO terms and gene products based on their GO annotation. Moreover it allows for computing a GO enrichment analysis
	"""
	
	bioc = "GOSim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GOSim_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GOSim/GOSim_1.40.0.tar.gz"]

	version("1.40.0", sha256="61af6af473c9525fec92119d5c0e9e07c2e1d61ff31fefacb80c87488796fac7")

	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
