# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFiles(RPackage):
	"""Effective File Navigation from the R Console

	Functions for printing the contents of a folder as columns in a ragged-bottom data.frame and for
  viewing the details (size, time created, time modified, etc.) of a folder's top level contents.
	"""
	
	cran = "files" 

	version("0.0.1", md5="1ede381fd55532d7ea70f93784fb6f23")

	depends_on("r@3.3.1:", type=("build", "run"))
