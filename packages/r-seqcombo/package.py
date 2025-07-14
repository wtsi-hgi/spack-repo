# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcombo(RPackage):
	"""Visualization Tool for Genetic Reassortment

	Provides useful functions for visualizing virus reassortment events.
	"""
	
	bioc = "seqcombo" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seqcombo_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seqcombo/seqcombo_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="8a780338f42603de0d7d8b517f456d2a65f2291e8764f19b98fb831b21767bf7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
