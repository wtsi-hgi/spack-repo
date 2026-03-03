# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhpl(RPackage):
	"""Ordered Homogeneity Pursuit Lasso for Group Variable Selection

	Ordered homogeneity pursuit lasso (OHPL)
    algorithm for group variable selection proposed in Lin et al. (2017)
    <DOI:10.1016/j.chemolab.2017.07.004>. The OHPL method exploits the
    homogeneity structure in high-dimensional data and enjoys the
    grouping effect to select groups of important variables
    automatically. This feature makes it particularly useful for
    high-dimensional datasets with strongly correlated variables,
    such as spectroscopic data.
	"""
	
	homepage = "https://ohpl.io"
	cran = "OHPL" 

	version("1.4", md5="e4db1acb15b618e2a142a284c8019df0")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
