# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGscounts(RPackage):
	"""Group Sequential Designs with Negative Binomial Outcomes

	Design and analysis of group sequential designs for negative
    binomial outcomes, as described by T Mütze, E Glimm, H Schmidli, T Friede (2018) <doi:10.1177/0962280218773115>.
	"""
	
	homepage = "https://github.com/tobiasmuetze/gscounts"
	cran = "gscounts" 

	version("0.1-4", md5="2fc7e6a6697c6b5677f641420d215937")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
