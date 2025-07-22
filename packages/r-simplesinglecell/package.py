# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplesinglecell(RPackage):
	"""A step-by-step workflow for low-level analysis of single-cell RNA-seq data with Bioconductor

	Once a proud workflow package, this is now a shell of its former self. Almost all of its content has been cannibalized for use in the "Orchestrating Single-Cell Analyses with Bioconductor" book at https://osca.bioconductor.org. Most vignettes here are retained as reminders of the glory that once was, also providing redirection for existing external links to the relevant OSCA book chapters.
	"""

	homepage = "https://www.bioconductor.org/help/workflows/simpleSingleCell/"
	bioc = "simpleSingleCell"version("1.32.0", commit="bdbb2453d3d84b91cdd63a6b146a34875f23450d")
	version("1.26.0", commit="ad07eabce25b0dc91f4eb97f15230f8b0616a186")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-codedepends", type=("build", "run"))
