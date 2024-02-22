# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSticky(RPackage):
	"""Persist Attributes Across Data Operations

	In base R, object attributes are lost when objects are modified by
    common data operations such as subset, filter, slice, append, extract
    etc. This packages allows objects to be marked as 'sticky' and have
    attributes persisted during these operations or when inserted
    into or extracted from list-like or table-like objects.
	"""
	
	homepage = "https://github.com/decisionpatterns/sticky"
	cran = "sticky" 

	version("0.5.6.1", md5="f9293d736d311f1b3ed167fc55b6f8f9")

	depends_on("r@3.1:", type=("build", "run"))
