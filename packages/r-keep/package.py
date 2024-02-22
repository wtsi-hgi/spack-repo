# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeep(RPackage):
	"""Arrays with Better Control over Dimension Dropping

	Provides arrays with flexible control over dimension dropping when subscripting.
	"""
	
	cran = "keep" 

	version("1.0", md5="93e7009249cb919f081d11b277bb82f5")

