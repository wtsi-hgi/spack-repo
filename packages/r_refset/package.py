# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefset(RPackage):
	"""Subsets with Reference Semantics

	Provides subsets with reference semantics, i.e. subsets
    which automatically reflect changes in the original object, and which
    optionally update the original object when they are changed.
	"""
	
	homepage = "http://github.com/hughjonesd/refset"
	cran = "refset" 

	version("0.1.1", md5="303c7612b69bf588a3cc9d0d56923494")

