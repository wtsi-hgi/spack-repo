# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrho(RPackage):
	"""Inference on agreement between ordered lists

	The package is aimed at inference on the amount of agreement in two sorted lists using the Rank-Rank Hypergeometric Overlap test.
	"""
	
	bioc = "RRHO" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RRHO_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RRHO/RRHO_1.42.0.tar.gz"]

	version("1.42.0", md5="979e74a493ef06b25a98574facdd4c3f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
