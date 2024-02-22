# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElastes(RPackage):
	"""Elastic Full Procrustes Means for Sparse and Irregular Planar
Curves

	Provides functions for the computation of functional elastic shape 
  means over sets of open planar curves. The package is particularly suitable for 
  settings where these curves are only sparsely and irregularly observed. It uses 
  a novel approach for elastic shape mean estimation, where planar curves are
  treated as complex functions and a full Procrustes mean is estimated from the
  corresponding smoothed Hermitian covariance surface. This is combined with the 
  methods for elastic mean estimation proposed in Steyer, Stöcker, Greven	(2022)
  <doi:10.1111/biom.13706>. See Stöcker et. al. (2022) <arXiv:2203.10522> for details.
	"""
	
	homepage = "https://mpff.github.io/elastes/"
	cran = "elastes" 

	version("0.1.7", md5="8fcd2852ac1d175123b4d6b088367b2e")

	depends_on("r-elasdics", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sparseflmm", type=("build", "run"))
	depends_on("r-orthogonalsplinebasis", type=("build", "run"))
