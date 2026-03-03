# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatticekrig(RPackage):
	"""Multi-Resolution Kriging Based on Markov Random Fields

	Methods for the interpolation of large spatial
  datasets. This package follows a "fixed rank Kriging" approach but
  provides a surface fitting method
  that can approximate standard spatial data models.
  Using a large number of basis functions allows for estimates that
  can come close to interpolating the observations (a spatial model
  with a small nugget variance.)  Moreover, the covariance model for
  this method can approximate the Matern covariance family but also
  allows for a multi-resolution model and supports efficient
  computation of the profile likelihood for estimating covariance
  parameters. This is accomplished through compactly supported basis
  functions and a Markov random field model for the basis
  coefficients. These features lead to sparse matrices for the
  computations and this package makes of the R spam package for sparse
  linear algebra.
  An extension of this version over previous ones ( < 5.4 ) is the
  support for different geometries besides a rectangular domain. The
  Markov random field approach combined with a basis function
  representation makes the implementation of different geometries
  simple where only a few specific R functions need to be added with
  most of the computation and evaluation done by generic routines that
  have been tuned to be efficient.  One benefit of this package's
  model/approach is the facility to do unconditional and conditional
  simulation of the field for large numbers of arbitrary points. There
  is also the flexibility for estimating non-stationary covariances
  and also the case when the observations are a linear combination
  (e.g. an integral) of the spatial process. Included are generic
  methods for prediction, standard errors for prediction, plotting of
  the estimated surface and conditional and unconditional simulation.
  See the 'LatticeKrig' GitHub repository for a vignette of this package.
  Development of this package was supported in part by the National
  Science Foundation  Grant 1417857 and the National Center for
  Atmospheric Research. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "LatticeKrig" 

	version("8.4", md5="508dd6a33a040d1d5e0c366df27e3f0d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-fields@9.9:", type=("build", "run"))
