# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeshr(RPackage):
	"""Tools for conducting enrichment analysis of MeSH

	A set of annotation maps describing the entire MeSH assembled using data from MeSH.
	"""
	
	bioc = "meshr"

	version("2.14.0", commit="7e4fb6bcd3e0017f18a67a50fd6509b88f3c1566")
	version("2.8.0", commit="4fc2782e367bf57742ae459edf7847964906b11f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-meshdbi", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
