# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSm(RPackage):
	"""Smoothing Methods for Nonparametric Regression and Density Estimation.

	This is software linked to the book 'Applied Smoothing Techniques for Data
	Analysis - The Kernel Approach with S-Plus Illustrations' Oxford University
	Press."""

	cran = "sm"

	license("GPL-2.0-or-later")

	version("2.2-6.0", md5="c09c5d6260479b702349067c2bd3588c")

	depends_on("r@3.1:", type=("build", "run"))
