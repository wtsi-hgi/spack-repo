# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathrender(RPackage):
	"""Render molecular pathways

	build graphs from pathway databases, render them by Rgraphviz.
	"""
	
	homepage = "http://www.bioconductor.org"
	bioc = "pathRender"

	version("1.76.0", commit="c7cec6a231c00eb9d3bd5a02f3cbff445924abec")
	version("1.70.0", commit="1fa46b59693d2716c7ee74ddbccc892884e7828c")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cmap", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
