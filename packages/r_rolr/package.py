# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolr(RPackage):
	"""Finding Optimal Three-Group Splits Based on a Survival Outcome

	Provides fast procedures for exploring all pairs of
    cutpoints of a single covariate with respect to survival and determining
    optimal cutpoints using a hierarchical method and various ordered logrank tests.
	"""
	
	cran = "rolr" 

	version("1.0.0", md5="e4505d5618a3cb8a9d0452b7c37331a4")

	depends_on("r-survival", type=("build", "run"))
