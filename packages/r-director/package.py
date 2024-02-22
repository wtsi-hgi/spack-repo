# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirector(RPackage):
	"""A dynamic visualization tool of multi-level data

	Director is an R package designed to streamline the visualization of molecular effects in regulatory cascades. It utilizes the R package htmltools and a modified Sankey plugin of the JavaScript library D3 to provide a fast and easy, browser-enabled solution to discovering potentially interesting downstream effects of regulatory and/or co-expressed molecules. The diagrams are robust, interactive, and packaged as highly-portable HTML files that eliminate the need for third-party software to view. This enables a straightforward approach for scientists to interpret the data produced, and bioinformatics developers an alternative means to present relevant data.
	"""
	
	homepage = "https://github.com/kzouchka/Director"
	bioc = "Director" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Director_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Director/Director_1.28.0.tar.gz"]

	version("1.28.0", md5="7c6c9d1a4762ffbdf723111273ee0899")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
