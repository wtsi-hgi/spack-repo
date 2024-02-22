# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcov(RPackage):
	"""Sparse Estimation of a Covariance Matrix

	Provides a covariance estimator for multivariate normal
        data that is sparse and positive definite.  Implements the
        majorize-minimize algorithm described in Bien, J., and
        Tibshirani, R. (2011), "Sparse Estimation of a Covariance
        Matrix," Biometrika. 98(4). 807--820.
	"""
	
	cran = "spcov" 

	version("1.3", md5="0648d330faa1164150737f6e1f6fa493")

