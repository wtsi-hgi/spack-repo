# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoc(RPackage):
	"""utilities for ROC, with microarray focus.

	Provide utilities for ROC, with microarray focus."""

	bioc = "ROC"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ROC_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ROC/ROC_1.78.0.tar.gz"]

	version("1.78.0", md5="2b84dc68639bbe6dbc5e4b9eeb429dbb")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
