# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmapr(RPackage):
	"""CMap Tools in R

	The Connectivity Map (CMap) is a massive resource of perturbational gene expression profiles built by researchers at the Broad Institute and funded by the NIH Library of Integrated Network-Based Cellular Signatures (LINCS) program. Please visit https://clue.io for more information. The cmapR package implements methods to parse, manipulate, and write common CMap data objects, such as annotated matrices and collections of gene sets.
	"""
	
	homepage = "https://github.com/cmap/cmapR"
	bioc = "cmapR"

	version("1.20.0", commit="9b120614372b497c8c663cb0ccb450ab2a4965d8")
	version("1.14.0", commit="34c94ada3dc345694a818f3c1fcbf07be8804263")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
