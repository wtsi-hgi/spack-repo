# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStcov(RPackage):
	"""Stein's Covariance Estimator

	Estimates a covariance matrix using Stein's isotonized covariance
    estimator, or a related estimator suggested by Haff.
	"""
	
	cran = "stcov" 

	version("0.1.0", md5="f27118978076854cb94231efaacc844e")

