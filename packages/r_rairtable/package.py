# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRairtable(RPackage):
	"""Efficient Wrapper for the 'Airtable' API

	Efficient CRUD interface for the 'Airtable' API <https://airtable.com/developers/web/api>, supporting batch requests and parallel encoding of large data sets.
	"""
	
	homepage = "https://matthewjrogers.github.io/rairtable/"
	cran = "rairtable" 

	version("0.1.2", md5="7cd02dc8923a5b7ceb07e2abee6723f3")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
