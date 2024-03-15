# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolspline(RPackage):
	"""Polynomial Spline Routines.

	Routines for the polynomial spline fitting routines hazard regression,
	hazard estimation with flexible tails, logspline, lspec, polyclass, and
	polymars, by C. Kooperberg and co-authors."""

	cran = "polspline"

	license("GPL-2.0-or-later")

	version("1.1.24", md5="7425c2c2ac60df9780e13876a94de9b9")

