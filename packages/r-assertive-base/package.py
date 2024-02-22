# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertiveBase(RPackage):
	"""A Lightweight Core of the 'assertive' Package.

	A minimal set of predicates and assertions used by the assertive package.
	This is mainly for use by other package developers who want to include
	run-time testing features in their own packages. End-users will usually
	want to use assertive directly."""

	cran = "assertive.base"

	version("0.0-9", md5="a2ee821abdf770469319622fc5508ce4")

	depends_on("r@3.5:", type=("build", "run"))
