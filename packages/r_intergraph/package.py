# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntergraph(RPackage):
	"""Coercion Routines for Network Data Objects

	Functions implemented in this package allow to coerce (i.e.
	convert) network data between classes provided by other R packages.
	Currently supported classes are those defined in packages: network and
	igraph.
	"""
	
	homepage = "https://mbojan.github.io/intergraph/"
	cran = "intergraph" 

	version("2.0-4", md5="09b8ba09e2989387378b2cae380ef025")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-network@1.4.2:", type=("build", "run"))
	depends_on("r-igraph@0.6.0:", type=("build", "run"))
