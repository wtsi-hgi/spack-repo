# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImprecise101(RPackage):
	"""Introduction to Imprecise Probabilities

	An imprecise inference presented in the study of Walley (1996) <doi:10.1111/j.2517-6161.1996.tb02065.x> is one of the statistical reasoning methods when prior information is unavailable. Functions and utils needed for illustrating this inferential paradigm are implemented for classroom teaching and further comprehensive research. Two imprecise models are demonstrated using multinomial data and 2x2 contingency table data. The concepts of prior ignorance and imprecision are discussed in lower and upper probabilities. Representation invariance principle, hypothesis testing, decision-making, and further generalization are also illustrated.
	"""
	
	cran = "imprecise101" 

	version("0.2.2.4", md5="26674d82c41e13846c95f3d0248b2188", url="https://cran.r-project.org/src/contrib/imprecise101_0.2.2.4.tar.gz")

	depends_on("r-tolerance", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
