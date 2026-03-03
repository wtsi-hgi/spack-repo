# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiagrammersvg(RPackage):
	"""Export DiagrammeR Graphviz Graphs as SVG

	Allows for export of DiagrammeR Graphviz objects to SVG.
	"""
	
	homepage = "https://github.com/rich-iannone/DiagrammeRsvg"
	cran = "DiagrammeRsvg" 

	version("0.1", md5="3b2984c227d516c9578982c9faa89456")

	depends_on("r-v8@0.10:", type=("build", "run"))
