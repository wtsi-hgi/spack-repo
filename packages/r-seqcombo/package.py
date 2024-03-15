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

	version("1.24.0", md5="76a401edd5e5583a94ab3a1b599b7a78")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
