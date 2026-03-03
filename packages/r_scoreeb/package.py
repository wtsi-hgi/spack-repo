# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoreeb(RPackage):
	"""Score Test Integrated with Empirical Bayes for Association Study

	Perform association test within linear mixed model framework using score test integrated with Empirical Bayes for genome-wide association study. Firstly, score test was conducted for each marker under linear mixed model framework, taking into account the genetic relatedness and population structure. And then all the potentially associated markers were selected with a less stringent criterion. Finally, all the selected markers were placed into a multi-locus model to identify the true quantitative trait nucleotide.
	"""
	
	cran = "ScoreEB" 

	version("0.1.1", md5="33c18b29b2128536ab4afcaf4bf9f5e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
