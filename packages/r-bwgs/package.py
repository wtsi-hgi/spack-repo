# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBwgs(RPackage):
	"""BreedWheat Genomic Selection Pipeline

	Package for Breed Wheat Genomic Selection Pipeline. 
    The R package 'BWGS' is developed by Louis Gautier Tran <louis.gautier.tran@gmail.com> and Gilles Charmet <gilles.charmet@inra.fr>.
    This repository is forked from original repository <https://forgemia.inra.fr/umr-gdec/bwgs>
    and modified as a R package.
	"""
	
	homepage = "https://github.com/byzheng/BWGS"
	cran = "BWGS" 

	version("0.2.1", md5="14cd984fd1bd2d21830b6164936940f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
	depends_on("r-bglr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-brnn", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
