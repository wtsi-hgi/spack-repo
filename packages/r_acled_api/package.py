# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcledApi(RPackage):
	"""Automated Retrieval of ACLED Conflict Event Data

	Access and manage the application programming interface (API) of the Armed Conflict Location & Event Data Project (ACLED) at <https://acleddata.com/>. The package makes it easy to retrieve a user-defined sample (or all of the available data) of ACLED, enabling a seamless integration of regular data updates into the research work flow. It requires a minimal number of dependencies. See the package's README file for a note on replicability when drawing on ACLED data. When using this package, you acknowledge that you have read ACLED's terms and conditions of use, and that you agree with their attribution requirements.
	"""
	
	homepage = "<https://gitlab.com/chris-dworschak/acled.api>"
	cran = "acled.api" 

	version("1.1.7", md5="bf3315d9b1c04ff0159258bd9ffd6cc0")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
