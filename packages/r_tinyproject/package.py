# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinyproject(RPackage):
	"""A Lightweight Template for Data Analysis Projects

	Creates useful files and folders for data
  analysis  projects and provides functions to manage data,
  scripts and output files. Also provides a project
  template for 'Rstudio'.
	"""
	
	cran = "tinyProject" 

	version("0.6.1", md5="7a304318064a4c861d7fe2f56fa0a4fa")

	depends_on("r-brew", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
