# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGagblup(RPackage):
	"""Genetic Algorithm Assisted Genomic Best Liner Unbiased
Prediction

	Performs genetic algorithm (Scrucca, L (2013) <doi:10.18637/jss.v053.i04>) 
             assisted genomic best liner unbiased prediction for genomic selection.
             It also provides a binning method in natural population for genomic selection
             under the principle of linkage disequilibrium for dimensional reduction.
	"""
	
	cran = "GAGBLUP" 

	version("1.0", md5="309a75f7b813ce48b7e64fcd57961a10")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
