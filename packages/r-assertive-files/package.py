# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertiveFiles(RPackage):
	"""Assertions to Check Properties of Files.

	A set of predicates and assertions for checking the properties of files and
	connections. This is mainly for use by other package developers who want to
	include run-time testing features in their own packages. End-users will
	usually want to use assertive directly."""

	cran = "assertive.files"

	version("0.0-2", md5="6ec546e99c6466feffca3ab09a670c76")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertive-base@0.0.2:", type=("build", "run"))
	depends_on("r-assertive-numbers", type=("build", "run"))
