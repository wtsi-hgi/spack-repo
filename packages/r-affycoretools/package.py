# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffycoretools(RPackage):
	"""Functions useful for those doing repetitive analyses with Affymetrix
	GeneChips.

	Various wrapper functions that have been written to streamline the more
	common analyses that a core Biostatistician might see."""

	bioc = "affycoretools"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/affycoretools_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/affycoretools/affycoretools_1.74.0.tar.gz"]

	version("1.74.0", md5="0e35c33fb3f3a4cdc7778efacbc45441")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-reportingtools", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-glimma", type=("build", "run"))
