# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdsr(RPackage):
	"""Complement to 'Modern Data Science with R'

	A complement to *Modern Data
    Science with R*, both the first 
    and second editions (ISBN: 978-0367191498, publisher URL: 
    <https://www.routledge.com/Modern-Data-Science-with-R/Baumer-Kaplan-Horton/p/book/9780367191498>).
    This package contains data and code to complete exercises and 
    reproduce examples from the text. It also facilitates connections 
    to the SQL database server used in the book. Both editions of the book are 
    supported by this package.
	"""
	
	homepage = "https://github.com/mdsr-book/mdsr"
	cran = "mdsr" 

	version("0.2.7", md5="498c43b4cfae6dcce88719d1ebb6e511")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-babynames", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rmariadb", type=("build", "run"))
	depends_on("r-skimr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
