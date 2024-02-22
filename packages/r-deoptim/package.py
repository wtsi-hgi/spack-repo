# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RDeoptim(RPackage):
	"""Global Optimization by Differential Evolution.

	Implements the differential evolution algorithm for global optimization of
	a real-valued function of a real-valued parameter vector."""

	cran = "DEoptim"

	version("2.2-8", md5="8640e68c8895aeabe5d3ff3d79f64392")

