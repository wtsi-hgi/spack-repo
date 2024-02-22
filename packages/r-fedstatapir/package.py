# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFedstatapir(RPackage):
	"""Unofficial API for Fedstat (Rosstat EMISS System) for Automatic
and Efficient Data Queries

	An API for automatic data queries to the fedstat <https://www.fedstat.ru>, using a small set of functions with a common interface.
	"""
	
	homepage = "https://github.com/DenchPokepon/fedstatAPIr"
	cran = "fedstatAPIr" 

	version("1.0.3", md5="f80bf0b82dfd688e80c5eb6c3aaca3ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-readsdmx", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
