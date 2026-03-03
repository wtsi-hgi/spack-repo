# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtreat(RPackage):
	"""A Statistically Sound 'data.frame' Processor/Conditioner

	A 'data.frame' processor/conditioner that prepares real-world data for predictive modeling in a statistically sound manner.
    'vtreat' prepares variables so that data has fewer exceptional cases, making
    it easier to safely use models in production. Common problems 'vtreat' defends
    against: 'Inf', 'NA', too many categorical levels, rare categorical levels, and new
    categorical levels (levels seen during application, but not during training). Reference: 
    "'vtreat': a data.frame Processor for Predictive Modeling", Zumel, Mount, 2016, <DOI:10.5281/zenodo.1173313>.
	"""
	
	homepage = "https://github.com/WinVector/vtreat/"
	cran = "vtreat" 

	version("1.6.4", md5="2b45dd40ee1982f7fd5b245047479191")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-wrapr@2.0.9:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
