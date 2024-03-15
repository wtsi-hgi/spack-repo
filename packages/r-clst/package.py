# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClst(RPackage):
	"""Classification by local similarity threshold

	Package for modified nearest-neighbor classification based on calculation of a similarity threshold distinguishing within-group from between-group comparisons.
	"""
	
	bioc = "clst" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clst_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clst/clst_1.50.0.tar.gz"]

	version("1.50.0", md5="5988cf1c0b5207d2f78f75dbe6f2b467")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
