# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNleqslv(RPackage):
	"""Solve Systems of Nonlinear Equations.

	Solve a system of nonlinear equations using a Broyden or a Newton method
	with a choice of global strategies such as line search and trust region.
	There are options for using a numerical or user supplied Jacobian, for
	specifying a banded numerical Jacobian and for allowing a singular or
	ill-conditioned Jacobian."""

	cran = "nleqslv"

	version("3.3.5", md5="156b1b2aa6fb3d7d2a08ee869a6c42a1")

