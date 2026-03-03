# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorem(RPackage):
	"""Generate Lorem Ipsum Text

	Quickly generate lorem ipsum placeholder text. Easy to
    integrate in RMarkdown documents. Includes an RStudio addin to insert
    lorem ipsum into the current document.
	"""
	
	homepage = "https://github.com/gadenbuie/lorem"
	cran = "lorem" 

	version("1.0.0", md5="e482456963180c957f2dad9c1b5d6bc0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
