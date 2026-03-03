# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGithubinstall(RPackage):
	"""A Helpful Way to Install R Packages Hosted on GitHub

	Provides an helpful way to install packages hosted on GitHub.
	"""
	
	homepage = "https://github.com/hoxo-m/githubinstall"
	cran = "githubinstall" 

	version("0.2.2", md5="4601fa31eabe8091685b0da056fe064b")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mockery", type=("build", "run"))
