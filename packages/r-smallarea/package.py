# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmallarea(RPackage):
	"""Fits a Fay Herriot Model

	Inference techniques for Fay Herriot Model.
	"""
	
	cran = "smallarea" 

	version("0.1", md5="ca16331a4771db7323752c50dba0c123")

	depends_on("r-mass", type=("build", "run"))
