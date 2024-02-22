# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrew(RPackage):
	"""Templating Framework for Report Generation.

	Brew implements a templating framework for mixing text and R code for
	report generation. brew template syntax is similar to PHP, Ruby's erb
	module, Java Server Pages, and Python's psp module."""

	cran = "brew"

	version("1.0-10", md5="c1ebbea7284161a8884ffe9ae5ca451f")

