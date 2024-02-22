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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cmapR_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cmapR/cmapR_1.14.0.tar.gz"]

	version("1.14.0", md5="257c275c11341cac65aae8f0d8cd4e2f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
