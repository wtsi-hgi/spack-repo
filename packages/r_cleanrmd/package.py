# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleanrmd(RPackage):
	"""Clean Class-Less 'R Markdown' HTML Documents

	A collection of clean 'R Markdown' HTML document templates
    using classy-looking classless CSS styles. These documents use a
    minimal set of dependencies but still look great, making them suitable
    for use a package vignettes or for sharing results via email.
	"""
	
	homepage = "https://pkg.garrickadenbuie.com/cleanrmd/"
	cran = "cleanrmd" 

	version("0.1.1", md5="230c97ddceeff411aac73644f044fd9f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
