# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvjamdaData(RPackage):
	"""Data for Package 'survJambda'

	Three breast cancer gene expression data sets that can be used for package 'survJamda'. This package contains the gene expression and phenotype data of GSE1992, GSE3143 and GSE4335. 
	"""
	
	cran = "survJamda.data" 

	version("1.0.2", md5="127b220fbdbf3721980d66a6da4a5297")

	depends_on("r@2.10:", type=("build", "run"))
