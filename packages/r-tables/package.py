# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTables(RPackage):
	"""Formula-Driven Table Generation

	Computes and displays complex tables of summary statistics.
  Output may be in LaTeX, HTML, plain text, or an R
  matrix for further processing.
	"""
	
	homepage = "https://dmurdoch.github.io/tables/"
	cran = "tables" 

	version("0.9.17", md5="c4ae042cab095279b54293ac5190bbc6")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
