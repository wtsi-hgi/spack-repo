# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruh(RPackage):
	"""Two-Sample Nonparametric Testing Under Heterogeneity

	Implements the TRUH test statistic for two sample testing under heterogeneity. TRUH incorporates the underlying heterogeneity and imbalance in the samples, and provides a conservative test for the composite null hypothesis that the two samples arise from the 
   same mixture distribution but may differ with respect to the mixing weights. See Trambak Banerjee, Bhaswar B. Bhattacharya, Gourab Mukherjee Ann. Appl. Stat. 14(4): 1777-1805 (December 2020). <DOI:10.1214/20-AOAS1362> for more details.
	"""
	
	homepage = "https://github.com/natesmith07/truh"
	cran = "truh" 

	version("1.0.0", md5="a0d49aa2b7232c7f56c762a694e4b486")

	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
