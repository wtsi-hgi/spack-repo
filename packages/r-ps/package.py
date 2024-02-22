# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPs(RPackage):
	"""List, Query, Manipulate System Processes.

	List, query and manipulate all system processes, on 'Windows', 'Linux' and
	'macOS'."""

	cran = "ps"

	version("1.7.6", md5="9a1d826feaafb2150f5c35bec3ff7255")

	depends_on("r@3.4:", type=("build", "run"))
