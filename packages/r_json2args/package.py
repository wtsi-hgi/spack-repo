# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJson2args(RPackage):
	"""Parse Parameters Inside a Docker Container

	The function get_parameters() is intended to be used within a docker container to read keyword arguments from a .json file automagically. A tool.yaml file contains specifications on these keyword arguments, which are then passed as input to containerized R tools in the [tool-runner framework](<https://github.com/hydrocode-de/tool-runner>). A template for a containerized R tool, which can be used as a basis for developing new tools, is available at the following URL: <https://github.com/VForWaTer/tool_template_r>.
	"""
	
	homepage = "https://github.com/VForWaTer/json2aRgs"
	cran = "json2aRgs" 

	version("0.3.0", md5="7f3d79c2d32297f22ebc03241747e42f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
