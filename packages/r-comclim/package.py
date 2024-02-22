# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComclim(RPackage):
	"""Community Climate Statistics

	Computes community climate statistics for volume and mismatch using species' climate niches either unscaled or scaled relative to a regional species pool. These statistics can be used to describe biogeographic patterns and infer community assembly processes. Includes a vignette outlining usage.
	"""
	
	cran = "comclim" 

	version("0.9.6", md5="8d2edfb5acd3cdb89fce63ef5a3585f6")

	depends_on("r@3:", type=("build", "run"))
