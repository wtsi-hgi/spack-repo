# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiftr(RPackage):
	"""Containerize R Markdown Documents for Continuous Reproducibility

	Persistent reproducible reporting by containerization of R Markdown documents.
	"""
	
	homepage = "https://nanx.me/liftr/"
	cran = "liftr" 

	version("0.9.2", md5="3d4f527f4f1edbe3af951084b2f3bfa4")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
