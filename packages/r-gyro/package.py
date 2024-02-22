# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGyro(RPackage):
	"""Hyperbolic Geometry

	Hyperbolic geometry in the Minkowski model and the Poincaré
    model. The methods are based on the gyrovector space theory developed
    by A. A. Ungar that can be found in the book 'Analytic Hyperbolic
    Geometry: Mathematical Foundations And Applications'
    <doi:10.1142/5914>. The package provides functions to plot
    three-dimensional hyperbolic polyhedra and to plot hyperbolic tilings
    of the Poincaré disk.
	"""
	
	homepage = "https://github.com/stla/gyro"
	cran = "gyro" 

	version("1.4.0", md5="c962bc559ad78df0dccf6c82d828f02c")

	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-colorsgen", type=("build", "run"))
	depends_on("r-cxhull@0.3:", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-rcdt", type=("build", "run"))
