# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtodoist(RPackage):
	"""Create and Manage Todolist using 'Todoist.com' API

	Allows you to interact with the API of the "Todoist" platform.
    'Todoist' <https://todoist.com/> provides an online task manager service for teams.
	"""
	
	homepage = "https://github.com/ThinkR-open/rtodoist"
	cran = "rtodoist" 

	version("0.1.0", md5="02b05c3359b14df8a474f98d745ca1bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
