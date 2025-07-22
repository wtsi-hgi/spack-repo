# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocthis(RPackage):
	"""Automate package and project setup for Bioconductor packages

	This package expands the usethis package with the goal of helping automate the process of creating R packages for Bioconductor or making them Bioconductor-friendly.
	"""
	
	homepage = "https://github.com/lcolladotor/biocthis"
	bioc = "biocthis"

	version("1.18.0", commit="e21a75aea3ecddc7910c892ba672a62abb4db59a")
	version("1.12.0", commit="7a2bcb519c1d4f1c6a61a5ac4c6a9dde5287cbbe")

	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-usethis@2.0.1:", type=("build", "run"))
