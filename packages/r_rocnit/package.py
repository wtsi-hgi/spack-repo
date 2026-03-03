# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocnit(RPackage):
	"""Non-Inferiority Test for Paired ROC Curves

	
  Non-inferiority test and diagnostic test are very important in clinical trails.
  This package is to get a p value from the non-inferiority test for ROC curves from diagnostic test.   
	"""
	
	cran = "rocNIT" 

	version("1.0", md5="6687fda4a9823cf97cc0fc8f651594e0")

	depends_on("r@3.3.2:", type=("build", "run"))
