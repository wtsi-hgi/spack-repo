# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorfeeder(RPackage):
	"""Integration of CellNOptR to add missing links

	This package integrates literature-constrained and data-driven methods to infer signalling networks from perturbation experiments. It permits to extends a given network with links derived from the data via various inference methods and uses information on physical interactions of proteins to guide and validate the integration of links.
	"""
	
	bioc = "CNORfeeder" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CNORfeeder_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CNORfeeder/CNORfeeder_1.42.0.tar.gz"]

	version("1.42.0", md5="4dd8271e71505e41edc9509155cb4f9f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cellnoptr@1.4:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
