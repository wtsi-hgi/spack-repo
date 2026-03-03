# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepogenerator(RPackage):
	"""Generates a Project and Repo for Easy Initialization of a
Workshop

	Generates a project and repo for easy initialization of a GitHub repo for R workshops. The repo includes a README with instructions to ensure that all users have the needed packages, an 'RStudio' project with the right directories and the proper data. The repo can then be used for hosting code taught during the workshop.
	"""
	
	homepage = "https://github.com/jaredlander/RepoGenerator"
	cran = "RepoGenerator" 

	version("0.0.1", md5="2a2f9ff3a22139f3abae625d73003adb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
