# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuotedargs(RPackage):
	"""A Way of Writing Functions that Quote their Arguments

	A facility for writing functions that quote their arguments,
 may sometimes evaluate them in the environment where they were quoted,
 and may pass them as quoted to other functions.
	"""
	
	cran = "quotedargs" 

	version("0.1.3", md5="0d32b9270bf1e6f1e159a5625e6b69c7")

