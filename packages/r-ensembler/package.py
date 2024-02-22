# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsembler(RPackage):
	"""Ensemble Models in R

	Functions to use ensembles of several machine learning models
    specified in caret package.
	"""
	
	cran = "ensembleR" 

	version("0.1.0", md5="d5f486690e1469fc51c2b09c2da1e6a0")

	depends_on("r-caret@6.0.71:", type=("build", "run"))
