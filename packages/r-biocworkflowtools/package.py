# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocworkflowtools(RPackage):
	"""Tools to aid the development of Bioconductor Workflow packages

	Provides functions to ease the transition between Rmarkdown and LaTeX documents when authoring a Bioconductor Workflow.
	"""
	
	bioc = "BiocWorkflowTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocWorkflowTools_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocWorkflowTools/BiocWorkflowTools_1.28.0.tar.gz"]

	version("1.28.0", sha256="a512296cd5c5ed6a3d8874378f7f5b4cd620c35e17ada1ad2918ea7ca3a60756")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
