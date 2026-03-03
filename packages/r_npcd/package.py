# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcd(RPackage):
	"""Nonparametric Methods for Cognitive Diagnosis

	An array of nonparametric and parametric estimation methods for cognitive diagnostic models, including nonparametric classification of examinee attribute profiles, joint maximum likelihood estimation (JMLE) of examinee attribute profiles and item parameters, and nonparametric refinement of the Q-matrix, as well as conditional maximum likelihood estimation (CMLE) of examinee attribute profiles given item parameters and CMLE of item parameters given examinee attribute profiles. Currently the nonparametric methods in the package support both conjunctive and disjunctive models, and the parametric methods in the package support the DINA model, the DINO model, the NIDA model, the G-NIDA model, and the R-RUM model. 
	"""
	
	cran = "NPCD" 

	version("1.0-11", md5="e09ccec82bab9cb31f79a736ae19caef")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
