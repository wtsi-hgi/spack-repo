# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdecode(RPackage):
	"""Descent-Based Calibrated Optimal Direct Estimation

	Algorithms for solving a self-calibrated l1-regularized quadratic programming problem without parameter tuning. The algorithm, called DECODE, can handle high-dimensional data without cross-validation. It is found useful in high dimensional portfolio selection (see Pun (2018) <https://ssrn.com/abstract=3179569>) and large precision matrix estimation and sparse linear discriminant analysis (see Pun and Hadimaja (2019) <https://ssrn.com/abstract=3422590>).
	"""
	
	cran = "rDecode" 

	version("0.1.0", md5="aa8a475af95a31a08e9df53648fc6d93")

	depends_on("r@2.10:", type=("build", "run"))
