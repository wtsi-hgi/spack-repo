# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcdcquery(RPackage):
	"""Query the Attentional Control Data Collection

	Interact with the Attentional Control Data Collection (ACDC).
  Connect to the database via connect_to_db(), set filter arguments via add_argument()
  and query the database via query_db().
	"""
	
	homepage = "https://github.com/SLesche/acdc-query"
	cran = "acdcquery" 

	version("1.0.1", md5="c4e8283ab5df483eed40c9d20cd8714b")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
