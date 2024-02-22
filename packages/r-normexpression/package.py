# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormexpression(RPackage):
	"""Normalize Gene Expression Data using Evaluated Methods

	It provides a framework and a fast and simple way for researchers to evaluate methods (particularly some data-driven methods or their own methods) and then select a best one for data normalization in the gene expression analysis, based on the consistency of metrics and the consistency of datasets.
             Zhenfeng Wu, Weixiang Liu, Xiufeng Jin, Deshui Yu, Hua Wang, Gustavo Glusman, Max Robinson, Lin Liu, Jishou Ruan and Shan Gao (2018) <doi:10.1101/251140>.
	"""
	
	cran = "NormExpression" 

	version("0.1.0", md5="96156c3815347fcd9ef511bf144e6d6e")

	depends_on("r@2.10:", type=("build", "run"))
