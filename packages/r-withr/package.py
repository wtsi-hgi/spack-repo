# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWithr(RPackage):
	"""Run Code 'With' Temporarily Modified Global State.

	A set of functions to run code 'with' safely and temporarily modified
	global state. Many of these functions were originally a part of the
	'devtools' package, this provides a simple package with limited
	dependencies to provide access to these functions."""

	cran = "withr"

	license("MIT")

	version("3.0.0", md5="679bfba74027cca036aeca2b328ba997")

	depends_on("r@3.5:", type=("build", "run"))
