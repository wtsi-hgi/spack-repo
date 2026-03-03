# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimax(RPackage):
	"""The Minimax Distribution Family

	The minimax family of distributions is a two-parameter
        family like the beta family, but computationally a lot more
        tractible.
	"""
	
	cran = "minimax" 

	version("1.1.1", md5="28e52ad91aa966f7961c355cec40d1f3")

