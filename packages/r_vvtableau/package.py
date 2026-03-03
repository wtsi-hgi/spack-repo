# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvtableau(RPackage):
	"""R Interface for 'Tableau' Services

	Provides an R interface for interacting with the 'Tableau' Server.
    It allows users to perform various operations such as publishing workbooks, refreshing data extracts, 
    and managing users using the 'Tableau' REST API (see <https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref.htm> for details). Additionally, 
    it includes functions to perform manipulations on local 'Tableau' workbooks.
	"""
	
	homepage = "https://github.com/vusaverse/vvtableau"
	cran = "vvtableau" 

	version("0.6.0", md5="a48c4ce96ea03f48cb94d23e41723f3c")
	version("0.5.0", md5="f97cea7ab20d71f94360c82f0bf23723")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
