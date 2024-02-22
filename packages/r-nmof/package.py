# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmof(RPackage):
	"""Numerical Methods and Optimization in Finance.

	Functions, examples and data from the book "Numerical Methods and
	Optimization in Finance" by M. Gilli, D. Maringer and E. Schumann (2011),
	ISBN 978-0123756626. The package provides implementations of several
	optimisation heuristics, such as Differential Evolution, Genetic Algorithms
	and Threshold Accepting. There are also functions for the valuation of
	financial instruments, such as bonds and options, and functions that help
	with stochastic simulations."""

	cran = "NMOF"

	version("2.8-0", md5="f8afaf5756144bb12be3f622e5a8b03e")

	depends_on("r@3.5:", type=("build", "run"))
