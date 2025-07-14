# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnvilpublish(RPackage):
	"""Publish Packages and Other Resources to AnVIL Workspaces

	Use this package to create or update AnVIL workspaces from resources such as R / Bioconductor packages. The metadata about the package (e.g., select information from the package DESCRIPTION file and from vignette YAML headings) are used to populate the 'DASHBOARD'. Vignettes are translated to python notebooks ready for evaluation in AnVIL.
	"""
	
	bioc = "AnVILPublish" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AnVILPublish_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AnVILPublish/AnVILPublish_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="25a53ff66d7b3b21874b1a08d165e16fc6682e34d2b9ab4a3aa8c06110d9657a")

	depends_on("r-anvil", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
