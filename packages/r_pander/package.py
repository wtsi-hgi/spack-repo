# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPander(RPackage):
	"""An R 'Pandoc' Writer

	Contains some functions catching all messages, 'stdout' and other
    useful information while evaluating R code and other helpers to return user
    specified text elements (like: header, paragraph, table, image, lists etc.)
    in 'pandoc' markdown or several type of R objects similarly automatically
    transformed to markdown format. Also capable of exporting/converting (the
    resulting) complex 'pandoc' documents to e.g. HTML, 'PDF', 'docx' or 'odt'. This
    latter reporting feature is supported in brew syntax or with a custom reference
    class with a smarty caching 'backend'.
	"""
	
	homepage = "https://rapporter.github.io/pander/"
	cran = "pander" 

	version("0.6.5", md5="c451137b7d98612a9ab32d217d4b6878")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
