# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListenv(RPackage):
	"""Environments Behaving (Almost) as Lists.

	List environments are environments that have list-like properties. For
	instance, the elements of a list environment are ordered and can be
	accessed and iterated over using index subsetting."""

	cran = "listenv"

	version("0.9.1", md5="c9eb64179893d8a0e5851366c259ed54")

	depends_on("r@3.1.2:", type=("build", "run"))
