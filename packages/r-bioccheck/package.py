# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioccheck(RPackage):
	"""Bioconductor-specific package checks

	BiocCheck guides maintainers through Bioconductor best practicies. It runs Bioconductor-specific package checks by searching through package code, examples, and vignettes. Maintainers are required to address all errors, warnings, and most notes produced.
	"""
	
	homepage = "https://github.com/Bioconductor/BiocCheck"
	bioc = "BiocCheck"

	version("1.44.2", commit="c9bf2e865c393138acf2881870ebbc5aa678d3b9")
	version("1.38.2", commit="043a804d64a7c273df5d1f850d74d823a96ad7bd")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biocviews@1.33.7:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
