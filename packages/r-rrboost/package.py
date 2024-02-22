# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrboost(RPackage):
	"""A Robust Boosting Algorithm

	An implementation of robust boosting algorithms for regression in R. This includes the RRBoost method proposed in the paper "Robust Boosting for Regression Problems" (Ju X and Salibian-Barrera M. 2020) <doi:10.1016/j.csda.2020.107065> (to appear in Computational Statistics and Data Science). It also implements previously proposed boosting algorithms in the simulation section of the paper: L2Boost, LADBoost, MBoost (Friedman, J. H. (2001) <doi:10.1214/aos/1013203451>) and Robloss (Lutz et al. (2008) <doi:10.1016/j.csda.2007.11.006>).
	"""
	
	cran = "RRBoost" 

	version("0.1", md5="8b12ae2113e0b035087795f53fb7e35b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-robstattm", type=("build", "run"))
