# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastmatch(RPackage):
	"""Fast 'match()' Function.

	Package providing a fast match() replacement for cases that require
	repeated look-ups. It is slightly faster that R's built-in match() function
	on first match against a table, but extremely fast on any subsequent lookup
	as it keeps the hash table in memory."""

	cran = "fastmatch"

	version("1.1-4", md5="9ed826f639a8b6d4c8519c1062a3c109")

	depends_on("r@2.3:", type=("build", "run"))
