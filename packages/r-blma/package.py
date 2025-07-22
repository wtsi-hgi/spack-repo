# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlma(RPackage):
	"""BLMA: A package for bi-level meta-analysis

	Suit of tools for bi-level meta-analysis. The package can be used in a wide range of applications, including general hypothesis testings, differential expression analysis, functional analysis, and pathway analysis.
	"""
	
	bioc = "BLMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BLMA_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BLMA/BLMA_1.26.0.tar.gz"]

	version("1.26.0", sha256="6266555a3692e93f261ef3fac295917349759c8b5629ff79a7d3d4f6fa6c71ab")

	depends_on("r-rontotools", type=("build", "run"))
	depends_on("r-gsa", type=("build", "run"))
	depends_on("r-padog", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
