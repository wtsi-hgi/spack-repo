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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocWorkflowTools_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocWorkflowTools/BiocWorkflowTools_1.28.0.tar.gz"]

	version("1.28.0", md5="412d30d47953d51e35e9fa188e28841e")

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
