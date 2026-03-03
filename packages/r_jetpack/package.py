# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJetpack(RPackage):
	"""A Friendly Package Manager

	Manage project dependencies from your DESCRIPTION file. Create a reproducible virtual environment with minimal additional files in your project. Provides tools to add, remove, and update dependencies as well as install existing dependencies with a single function.
	"""
	
	homepage = "https://github.com/ankane/jetpack"
	cran = "jetpack" 

	version("0.5.5", md5="096de62ff38de471abff7c5f58a727c8")

	depends_on("r-renv@0.13.1:", type=("build", "run"))
	depends_on("r-remotes@2.0.3:", type=("build", "run"))
	depends_on("r-desc@1.2:", type=("build", "run"))
	depends_on("r-docopt@0.4:", type=("build", "run"))
