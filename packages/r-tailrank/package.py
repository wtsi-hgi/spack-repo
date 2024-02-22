# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTailrank(RPackage):
	"""The Tail-Rank Statistic

	Implements the tail-rank statistic for selecting biomarkers
  from a microarray data set, an efficient nonparametric test focused
  on the distributional tails. See
  <https://gitlab.com/krcoombes/coombeslab/-/blob/master/doc/papers/tolstoy-new.pdf>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "TailRank" 

	version("3.2.2", md5="3403969aa4184ec075db92de18426c03")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-oompabase@3.0.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-oompadata", type=("build", "run"))
