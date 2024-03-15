# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcosolver(RPackage):
	"""Embedded Conic Solver in R.

	R interface to the Embedded COnic Solver (ECOS), an efficient and robust C
	library for convex problems. Conic and equality constraints can be
	specified in addition to integer and boolean variable constraints for
	mixed-integer problems. This R interface is inspired by the python
	interface and has similar calling conventions."""

	cran = "ECOSolveR"

	version("0.5.5", md5="6eef63b5a9ca57cf252bdb4eb705bc9e")

