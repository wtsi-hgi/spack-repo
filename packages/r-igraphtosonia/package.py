# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgraphtosonia(RPackage):
	"""Convert iGraph graps to SoNIA .son files

	This program facilitates exporting igraph graphs to the
        SoNIA file format
	"""
	
	cran = "igraphtosonia" 

	version("1.0", md5="d76c91a1146e81bf3f8b54bb9bd6a12e")

	depends_on("r-igraph", type=("build", "run"))
