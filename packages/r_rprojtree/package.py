# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprojtree(RPackage):
	"""Create Folders and Files Structure for Data Science Projects

	Use JSON templates to create folders and files structure for data science projects. Includes customized templates and accepts your own as JSON files.
	"""
	
	homepage = "https://github.com/miguel-conde/rprojtree"
	cran = "rprojtree" 

	version("1.0.0", md5="f1fd0da7d54b4c8076d894c83a67fbf3")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
