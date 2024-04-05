# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrc(RPackage):
	"""Inference in Graphical Gaussian Models with Edge and Vertex
Symmetries

	Estimation, model selection and other aspects of
    statistical inference in Graphical Gaussian models with edge and
    vertex symmetries (Graphical Gaussian models with colours).
    Documentation about 'gRc' is provided in the paper by Hojsgaard and
    Lauritzen (2007, <doi:10.18637/jss.v023.i06>) and the paper by
    Hojsgaard and Lauritzen (2008, <doi:10.1111/j.1467-9868.2008.00666.x>).
	"""
	
	homepage = "https://people.math.aau.dk/~sorenh/software/gR/"
	cran = "gRc" 

	version("0.5.0", md5="8c1366601633200e5d3fa9aec9634826")
	version("0.4.6", md5="4e79edb86a97d121c118f2ae4dd59c0b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-grbase@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp@0.11.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
