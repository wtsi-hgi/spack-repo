# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvcanvas(RPackage):
	"""'Canvas' LMS API Integration

	Allow R users to interact with the 'Canvas' Learning Management System (LMS) API (see
    <https://canvas.instructure.com/doc/api/all_resources.html> for details).
    It provides a set of functions to access and manipulate course data, assignments, grades, users, 
    and other resources available through the 'Canvas' API.
	"""
	
	homepage = "https://github.com/vusaverse/vvcanvas"
	cran = "vvcanvas" 

	version("0.0.3", md5="1702d3d952144b46408b1964c74157c6")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htm2txt", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
