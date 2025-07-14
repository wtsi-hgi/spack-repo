# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenegeneinter(RPackage):
	"""Tools for Testing Gene-Gene Interaction at the Gene Level

	The aim of this package is to propose several methods for testing gene-gene interaction in case-control association studies. Such a test can be done by aggregating SNP-SNP interaction tests performed at the SNP level (SSI) or by using gene-gene multidimensionnal methods (GGI) methods. The package also proposes tools for a graphic display of the results. <doi:10.18637/jss.v095.i12>.
	"""
	
	bioc = "GeneGeneInteR"

	version("1.34.0", commit="9b29d5f9f317947e6569a0d66f973827e922695b")
	version("1.28.0", commit="5961a9fa0c9df843d1e719de1702239ed4473dd1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
