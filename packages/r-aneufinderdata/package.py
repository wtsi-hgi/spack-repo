# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAneufinderdata(RPackage):
	"""WGSCS Data for Demonstration Purposes.

	Whole-genome single cell sequencing data for demonstration purposes in
	the AneuFinder package."""

	bioc = "AneuFinderData"
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/AneuFinderData_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/AneuFinderData/AneuFinderData_1.30.0.tar.gz"]

	version("1.30.0", md5="895230cd9b780dbb286a012f3c8777eb")

	depends_on("r@3.3:", type=("build", "run"))

	# experiment