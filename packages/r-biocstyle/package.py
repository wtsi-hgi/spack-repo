# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocstyle(RPackage):
	"""Standard styles for vignettes and other Bioconductor documents.

	Provides standard formatting styles for Bioconductor PDF and HTML
	documents. Package vignettes illustrate use and functionality."""

	bioc = "BiocStyle"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocStyle_2.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocStyle/BiocStyle_2.30.0.tar.gz"]

	version("2.30.0", md5="22ceacb6ab374657de48283e78dedbb5")

	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-knitr@1.30:", type=("build", "run"))
	depends_on("r-rmarkdown@1.2:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
