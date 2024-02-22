# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialfdar(RPackage):
	"""Spatial Functional Data Analysis

	
  Finite element modeling (FEM) uses meshes of triangles to define surfaces.  
  A surface within a triangle may be either linear or quadratic. 
  In the order one case each node in the mesh is associated with a basis 
  function and the basis is called the order one finite element basis.
  In the order two case each edge mid-point is also associated with a basis
  function.  Functions are provided for smoothing, density function estimation
  point evaluation and plotting results.  Two papers illustrating the 
  finite element data analysis are Sangalli, L.M., Ramsay, J.O., 
  Ramsay, T.O. (2013)<http://www.mox.polimi.it/~sangalli> and
  Bernardi, M.S, Carey, M., Ramsay, J. O., Sangalli, L. 
  (2018)<http://www.mox.polimi.it/~sangalli>. Modelling 
  spatial anisotropy via regression with partial differential 
  regularization Journal of Multivariate Analysis, 167, 15-30.
	"""
	
	homepage = "http://www.functionaldata.org"
	cran = "SpatialfdaR" 

	version("1.0.0", md5="5a75ea8e9b500faefefded55e6639416")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
