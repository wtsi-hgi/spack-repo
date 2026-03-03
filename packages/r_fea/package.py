# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFea(RPackage):
	"""Finite Element Modeling for R

	Finite element modeling of beam structures and 2D geometries using constant strain triangles. Applies material properties and boundary conditions (load and constraint) to generate a finite element model. The model produces stress, strain, and nodal displacements; a heat map is available to demonstrate regions where output variables are high or low.  Also provides options for creating a triangular mesh of 2D geometries. Package developed with reference to: Bathe, K. J. (1996). Finite Element Procedures.[ISBN 978-0-9790049-5-7] -- Seshu, P. (2012). Textbook of Finite Element Analysis. [ISBN-978-81-203-2315-5] -- Mustapha, K. B. (2018). Finite Element Computations in Mechanics with R. [ISBN 9781315144474].
	"""
	
	cran = "FEA" 

	version("0.0.2", md5="be064f77402c7e354fdbcf800049ae64")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ptinpoly", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
