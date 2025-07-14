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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biocthis_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biocthis/biocthis_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="e8ad317d1599295e196f4274f08c84ad8947da4634c438eedc1cad080ed7ac53")

	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-usethis@2.0.1:", type=("build", "run"))
