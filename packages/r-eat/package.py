# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REat(RPackage):
	"""Efficiency Analysis Trees

	Functions are provided to determine production frontiers and technical 
    efficiency measures through non-parametric techniques based upon regression trees. 
    The package includes code for estimating radial input, output, directional and 
    additive measures, plotting graphical representations of the scores and the production 
    frontiers by means of trees, and determining rankings of importance of input variables 
    in the analysis. Additionally, an adaptation of Random Forest by a set of individual 
    Efficiency Analysis Trees for estimating technical efficiency is also included. More 
    details in: <doi:10.1016/j.eswa.2020.113783>.
	"""
	
	homepage = "https://efficiencytools.wordpress.com/"
	cran = "eat" 

	version("0.1.4", md5="ace9f5cf07235c227ae0777b5f794456")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-conflicted", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggparty", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
