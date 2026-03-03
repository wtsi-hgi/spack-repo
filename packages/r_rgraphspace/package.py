# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgraphspace(RPackage):
	"""A Lightweight Interface Between 'ggplot2' and 'igraph' Objects

	Interface to integrate 'igraph' and 'ggplot2' graphics within spatial maps. 'RGraphSpace' implements new geometric objects using 'ggplot2' prototypes, customized for representing large 'igraph' objects in a normalized coordinate system. By scaling shapes and graph elements, 'RGraphSpace' can provide a framework for layered visualizations.
	"""
	
	homepage = "https://github.com/sysbiolab/RGraphSpace"
	cran = "RGraphSpace" 

	version("1.0.5", md5="03147e75f7ae6334de33c4f023b931cd")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
