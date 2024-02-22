# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAods3(RPackage):
	"""Analysis of Overdispersed Data using S3 Methods

	Provides functions to analyse overdispersed
        counts or proportions.  These functions should be considered as
        complements to more sophisticated methods such as generalized
        estimating equations (GEE) or generalized linear mixed effect
        models (GLMM). aods3 is an S3 re-implementation of the
        deprecated S4 package aod.
	"""
	
	cran = "aods3" 

	version("0.4-1.2", md5="96cb3bd677824db4f5ab79ab07f37225", url="https://cran.r-project.org/src/contrib/aods3_0.4-1.2.tar.gz")

	depends_on("r@3:", type=("build", "run"))
