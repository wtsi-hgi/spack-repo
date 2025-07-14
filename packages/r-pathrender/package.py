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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pathRender_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pathRender/pathRender_1.70.0.tar.gz"]

	version("1.76.0", tag="RELEASE_3_21")
	version("1.70.0", sha256="1f5291482f1b0cd1722b62b3f10ac4a44b28419b793f86e6c7447ebb934b3212")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cmap", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
