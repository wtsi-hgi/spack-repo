# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnls(RPackage):
	"""The Lawson-Hanson algorithm for non-negative least squares (NNLS).

	An R interface to the Lawson-Hanson implementation of an algorithm for
	non-negative least squares (NNLS). Also allows the combination of
	non-negative and non-positive constraints."""

	cran = "nnls"

	license("GPL-2.0-or-later")

	version("1.5", md5="f1aaeef79fbbd3aee167b19b3f512e27")

