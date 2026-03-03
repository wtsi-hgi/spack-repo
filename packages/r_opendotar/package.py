# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpendotar(RPackage):
	"""Interface for OpenDota API

	Enables the usage of the OpenDota API from <https://www.opendota.com/>, get game lists, and download JSON's of parsed replays from
    the OpenDota API. Also has functionality to execute own code to extract the specific parts of the JSON file.
	"""
	
	cran = "opendotaR" 

	version("0.1.4", md5="846674f298e1414fe6425f220c7b40bb")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
