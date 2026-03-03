# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadtree(RPackage):
	"""Region Quadtrees for Spatial Data

	Provides functionality for working with raster-like quadtrees
    (also called “region quadtrees”), which allow for variable-sized
    cells. The package allows for flexibility in the quadtree creation
    process.  Several functions defining how to split and aggregate cells
    are provided, and custom functions can be written for both of these
    processes. In addition, quadtrees can be created using other quadtrees
    as “templates”, so that the new quadtree's structure is identical to
    the template quadtree. The package also includes functionality for
    modifying quadtrees, querying values, saving quadtrees to a file, and
    calculating least-cost paths using the quadtree as a resistance
    surface.
	"""
	
	homepage = "https://github.com/dfriend21/quadtree/"
	cran = "quadtree" 

	version("0.1.14", md5="22285241e858be6b2015701a3378c5bd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
