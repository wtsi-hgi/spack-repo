# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdm2id(RPackage):
	"""Data Mining and R Programming for Beginners

	Contains functions to simplify the use of data mining methods (classification, regression, clustering, etc.), for students and beginners in R programming. Various R packages are used and wrappers are built around the main functions, to standardize the use of data mining methods (input/output): it brings a certain loss of flexibility, but also a gain of simplicity. The package name came from the French "Fouille de Données en Master 2 Informatique Décisionnelle".
	"""
	
	cran = "fdm2id" 

	version("0.9.9", md5="8261cc0ae71019b7508fede8f834c34f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-arulesviz", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
