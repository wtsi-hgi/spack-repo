# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrobdingnag(RPackage):
	"""Very Large Numbers in R.

	Handles very large numbers in R. Real numbers are held using their natural
	logarithms, plus a logical flag indicating sign. The package includes a
	vignette that gives a step-by-step introduction to using S4 methods."""

	cran = "Brobdingnag"

	version("1.2-9", md5="0933a3366ef2f614998e8feee06473cc")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
