# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpslope(RPackage):
	"""Group Sorted L1 Penalized Estimation

	Group SLOPE (Group Sorted L1 Penalized Estimation) is
    a penalized linear regression method that is used for adaptive
    selection of groups of significant predictors in a high-dimensional
    linear model. The Group SLOPE method can control the (group) false
    discovery rate at a user-specified level (i.e., control the expected
    proportion of irrelevant among all selected groups of predictors).
    For additional information about the implemented methods please see
    Brzyski, Gossmann, Su, Bogdan (2018) <doi:10.1080/01621459.2017.1411269>.
	"""
	
	homepage = "https://github.com/agisga/grpSLOPE"
	cran = "grpSLOPE" 

	version("0.3.3", md5="67d62be9ddbd04012d80d09089ffceaa")

	depends_on("r-rcpp", type=("build", "run"))
