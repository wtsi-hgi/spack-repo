# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarter(RPackage):
	"""Starter Kit for New Projects

	Get started with new projects by dropping a skeleton of a new
    project into a new or existing directory, initialise git repositories,
    and create reproducible environments with the 'renv' package. The
    package allows for dynamically named files, folders, file content, as
    well as the functionality to drop individual template files into
    existing projects.
	"""
	
	homepage = "https://github.com/ddsjoberg/starter"
	cran = "starter" 

	version("0.1.14", md5="4d0a3ec1ddd0faaf41da53b1bcaa88b0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-gert@1.9.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-r-utils@2.11:", type=("build", "run"))
	depends_on("r-renv@0.17.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
