# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandpro(RPackage):
	"""Random Projection with Classification

	Performs random projection using Johnson-Lindenstrauss (JL) Lemma (see William B.Johnson and Joram Lindenstrauss (1984) <doi:10.1090/conm/026/737400>). Random Projection is a dimension reduction technique, where the data in the high dimensional space is projected into the low dimensional space using JL transform. The original high dimensional data matrix is multiplied with the low dimensional projection matrix which results in reduced matrix. The projection matrix can be generated using the projection function that is independent to the original data. Then finally apply the classification task on the projected data.  
	"""
	
	cran = "RandPro" 

	version("0.2.2", md5="d2f7502f872f56db4a2a0bc06964c2b5")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
