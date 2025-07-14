# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseede(RPackage):
	"""iSEE extension for panels related to differential expression analysis

	This package contains diverse functionality to extend the usage of the iSEE package, including additional classes for the panels or modes facilitating the analysis of differential expression results. This package does not perform differential expression. Instead, it provides methods to embed precomputed differential expression results in a SummarizedExperiment object, in a manner that is compatible with interactive visualisation in iSEE applications.
	"""
	
	homepage = "https://github.com/iSEE/iSEEde"
	bioc = "iSEEde" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iSEEde_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iSEEde/iSEEde_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="9cc20577ff9d5a98e2116dc0981f02885c0a620fd5ce3b887299c52c68332295")

	depends_on("r-isee", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
