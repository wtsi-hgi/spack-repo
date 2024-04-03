# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinship2(RPackage):
	"""Pedigree Functions

	Routines to handle family data with a pedigree object. The initial purpose
	     was to create correlation structures that describe family relationships such 
	     as kinship and identity-by-descent, which can be used to model family data 
	     in mixed effects models, such as in the coxme function. Also includes a tool
	     for pedigree drawing which is focused on producing compact layouts without 
	     intervention. Recent additions include utilities to trim the pedigree object
	     with various criteria, and kinship for the X chromosome.
	"""
	
	homepage = "https://cran.r-project.org/package=kinship2"
	cran = "kinship2" 

	version("1.9.6.1", md5="5da1437d1110095b1c15884f48a0de79", url="https://cran.r-project.org/src/contrib/kinship2_1.9.6.1.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
