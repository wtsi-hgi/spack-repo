# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHexview(RPackage):
	"""Viewing Binary Files

	Functions to view files in raw binary form like in a hex editor.  Additional functions to specify and read arbitrary binary formats.
	"""
	
	cran = "hexView" 

	version("0.3-4", md5="bef9f732bb59add40345f76ded0af94c")

	depends_on("r@1.8:", type=("build", "run"))
