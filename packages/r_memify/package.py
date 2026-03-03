# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemify(RPackage):
	"""Constructing Functions That Keep State

	A simple way to construct and maintain functions that keep state i.e. remember their argument lists. This can be useful when one needs to repeatedly invoke the same function with only a small number of argument changes at each invocation.
	"""
	
	cran = "memify" 

	version("0.1.1", md5="4656c740928a2e12fd1a5c910fd1f154")

	depends_on("r@4:", type=("build", "run"))
