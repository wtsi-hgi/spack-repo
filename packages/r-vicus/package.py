# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVicus(RPackage):
	"""Exploiting Local Structures to Improve Network-Based Analysis of
Biological Data

	Compared with the similar graph embedding method such as Laplacian Eigenmaps, 'Vicus' can exploit more local structures of graph data. For the details of the methods, see the reference section of 'GitHub' README.md <https://github.com/rikenbit/Vicus>.
	"""
	
	homepage = "https://github.com/rikenbit/Vicus"
	cran = "Vicus" 

	version("0.99.0", md5="3be479ec81a40a4d94ecc3e7753a6898")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
