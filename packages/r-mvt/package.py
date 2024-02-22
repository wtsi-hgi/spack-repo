# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvt(RPackage):
	"""Estimation and Testing for the Multivariate t-Distribution

	Routines to perform estimation and inference under the multivariate
  t-distribution <doi:10.1007/s10182-022-00468-2>. Currently, the following methodologies 
  are implemented: multivariate mean and covariance estimation, hypothesis testing 
  about equicorrelation and homogeneity of variances, the Wilson-Hilferty transformation, 
  QQ-plots with envelopes and random variate generation.
	"""
	
	homepage = "http://mvt.mat.utfsm.cl/"
	cran = "MVT" 

	version("0.3-8", md5="7448758ace3bf43d421976477815cae8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastmatrix", type=("build", "run"))
