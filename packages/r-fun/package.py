# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFun(RPackage):
	"""Use R for Fun

	This is a collection of R games and other funny stuff, such as the
    classic Mine sweeper and sliding puzzles.
	"""
	
	homepage = "https://github.com/yihui/fun"
	cran = "fun" 

	version("0.3", md5="4fd041251e5583817a86d6008611cf7f")

