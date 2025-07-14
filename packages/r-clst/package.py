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

    version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="824809724263d7dfbe27e8c153d4e2dee7b02bd8428090a712d0fcacd9947251")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
