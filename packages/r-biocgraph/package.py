# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocgraph(RPackage):
	"""Graph examples and use cases in Bioinformatics

	This package provides examples and code that make use of the different graph related packages produced by Bioconductor.
	"""
	
	bioc = "biocGraph"

	version("1.70.0", commit="f223484285d841dad3b29a785a68c33cac2139e4")
	version("1.64.0", commit="5928a24c8cac96dee813197c3d858f3896c52d7e")

	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
