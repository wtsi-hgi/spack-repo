# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheatsheet(RPackage):
	"""Download R Cheat Sheets Locally

	A simple package to grab cheat sheets and save them to your local computer.
	"""
	
	homepage = "https://bradlindblad.github.io/cheatsheet/"
	cran = "cheatsheet" 

	version("0.1.2", md5="8423d0827b45f0cc54934595769f106a")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
