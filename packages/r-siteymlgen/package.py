# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiteymlgen(RPackage):
	"""Automatically Generate _site.yml File for 'R Markdown'

	The goal of 'siteymlgen' is to make it easy to organise
  the building of your 'R Markdown' website.
  The init() function placed within the first code chunk of the index.Rmd
  file of an 'R' project directory will initiate the generation of an automatically
  written _site.yml file. 'siteymlgen' recommends a specific naming
  convention for your 'R Markdown' files. This naming will ensure that
  your navbar layout is ordered according to a hierarchy.
	"""
	
	homepage = "https://github.com/Acribbs/siteymlgen"
	cran = "siteymlgen" 

	version("1.0.0", md5="222007aecfecdc363d4841f0e047d8be")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ymlthis", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
