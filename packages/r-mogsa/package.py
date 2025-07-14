# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogsa(RPackage):
	"""Multiple omics data integrative clustering and gene set analysis

	This package provide a method for doing gene set analysis based on multiple omics data.
	"""
	
	bioc = "mogsa"

	version("1.42.0", commit="9b39a5c845a39fda7e0a2fd94778e564e4730b63")
	version("1.36.0", commit="2fb08c767830414ef2b62cf201e8bfd00ecd24d5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
