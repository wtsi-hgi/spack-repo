# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimorhyde(RPackage):
	"""Differential Analysis of Rhythmic Transcriptome Data

	A flexible approach, inspired by cosinor regression, for
  differential analysis of rhythmic transcriptome data. See Singer and Hughey
  (2018) <doi:10.1177/0748730418813785>.
	"""
	
	homepage = "https://limorhyde.hugheylab.org"
	cran = "limorhyde" 

	version("1.0.1", md5="d08d96bc24e8c5775922799bdffc4579")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pbs@1.1:", type=("build", "run"))
