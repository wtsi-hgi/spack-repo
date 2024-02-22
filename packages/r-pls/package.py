# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPls(RPackage):
	"""Partial Least Squares and Principal Component Regression.

	Multivariate regression methods Partial Least Squares Regression (PLSR),
	Principal Component Regression (PCR) and Canonical Powered Partial Least
	Squares (CPPLS)."""

	cran = "pls"

	version("2.8-3", md5="3206a18410583f0672f02cac9dbedce5")

	depends_on("r@3.5:", type=("build", "run"))
