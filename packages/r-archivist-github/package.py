# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchivistGithub(RPackage):
	"""Tools for Archiving, Managing and Sharing R Objects via GitHub

	The extension of the 'archivist' package integrating the archivist with GitHub via GitHub API, 'git2r' packages and 'httr' package. 
	"""
	
	homepage = "http://marcinkosinski.github.io/archivist.github/"
	cran = "archivist.github" 

	version("0.2.6", md5="8c5e2422686a8c9688aeedd128728017")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-archivist", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
