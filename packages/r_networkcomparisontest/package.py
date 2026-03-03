# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkcomparisontest(RPackage):
	"""Statistical Comparison of Two Networks Based on Several
Invariance Measures

	This permutation based hypothesis test, suited for several types of data 
    supported by the estimateNetwork function of the bootnet package (Epskamp & Fried, 2018), 
    assesses the difference between two networks based on several invariance measures (network 
    structure invariance, global strength invariance, edge invariance, several centrality 
    measures, etc.). Network structures are estimated with l1-regularization. The Network 
    Comparison Test is suited for comparison of independent (e.g., two different groups) and 
    dependent samples (e.g., one group that is measured twice). See van Borkulo et al. (2021),
    available from <doi:10.1037/met0000476>.
	"""
	
	cran = "NetworkComparisonTest" 

	version("2.2.2", md5="c699e7be5bafd726a02a5721f625b4cc")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-networktools", type=("build", "run"))
	depends_on("r-isingfit", type=("build", "run"))
