# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMockery(RPackage):
	"""Mocking Library for R.

	The two main functionalities of this package are creating mock objects
	(functions) and selectively intercepting calls to a given function that
	originate in some other function. It can be used with any testing framework
	available for R. Mock objects can be injected with either this package's
	own stub() function or a similar with_mock() facility present in the
	'testthat' package."""

	cran = "mockery"

	license("MIT")

	version("0.4.4", md5="98297a49097c3c952c9321de4710df7f")

	depends_on("r-testthat", type=("build", "run"))
