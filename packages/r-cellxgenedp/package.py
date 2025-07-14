# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellxgenedp(RPackage):
	"""Discover and Access Single Cell Data Sets in the cellxgene Data Portal

	The cellxgene data portal (https://cellxgene.cziscience.com/) provides a graphical user interface to collections of single-cell sequence data processed in standard ways to 'count matrix' summaries. The cellxgenedp package provides an alternative, R-based inteface, allowind data discovery, viewing, and downloading.
	"""
	
	homepage = "https://mtmorgan.github.io/cellxgenedp/"
	bioc = "cellxgenedp"

	version("1.12.1", commit="14ad312c264d783f1d4b87a264e2356b4ab1a76a")
	version("1.6.1", md5="dc1730a545f49b0b8c14991289f29a6b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rjsoncons", type=("build", "run"))
