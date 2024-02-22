# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgdex(RPackage):
	"""Agreement of Differential Expression Analysis.

	A tool to evaluate agreement of differential expression for cross-
	species genomics"""

	bioc = "AGDEX"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AGDEX_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AGDEX/AGDEX_1.50.0.tar.gz"]

	version("1.50.0", md5="9e74a7202bdc2e422e2213f1fb7a23f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
