# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostlogic(RPackage):
	"""Infix and Postfix Logic Operators

	Provides adds postfix and infix logic operators for
    if, then, unless, and otherwise.
	"""
	
	homepage = "https://github.com/RDocTaskForce/postlogic"
	cran = "postlogic" 

	version("0.1.0.1", md5="328a8d1e97a619777588275615523fa9")

