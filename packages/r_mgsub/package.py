# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgsub(RPackage):
	"""Safe, Multiple, Simultaneous String Substitution

	Designed to enable simultaneous substitution in strings in a safe fashion.
    Safe means it does not rely on placeholders (which can cause errors in same length matches).
	"""
	
	cran = "mgsub" 

	version("1.7.3", md5="1e204bdcd5b82c12f9cc0ebdd9bc3621")

