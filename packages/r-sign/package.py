# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSign(RPackage):
	"""Similarity Identification in Gene Expression

	Provides a classification framework to use expression patterns of pathways as features to identify similarity between biological samples. It provides a new measure for quantifying similarity between expression patterns of pathways.
	"""
	
	cran = "SIGN" 

	version("0.1.0", md5="c5e3aae7df9da712e929b6364528038b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
