# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneplast(RPackage):
	"""Evolutionary and plasticity analysis of orthologous groups

	Geneplast is designed for evolutionary and plasticity analysis based on orthologous groups distribution in a given species tree. It uses Shannon information theory and orthologs abundance to estimate the Evolutionary Plasticity Index. Additionally, it implements the Bridge algorithm to determine the evolutionary root of a given gene based on its orthologs distribution.
	"""
	
	bioc = "geneplast" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/geneplast_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/geneplast/geneplast_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="c215014d77c3f315c47e99ee2309243353a6c78b294928ebb163a52e8ae1e283")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
