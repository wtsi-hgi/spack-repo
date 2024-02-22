# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatabraryr(RPackage):
	"""Interact with the 'Databrary.org' API

	'Databrary.org' is a restricted access repository for research data, especially video and audio.
  This package provides commands to interact with the data stored on 'Databrary.org'.
	"""
	
	homepage = "https://github.com/databrary/databraryr"
	cran = "databraryr" 

	version("0.6.0", md5="6f012c806a50d58a03f9ce37b4f9f59f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
