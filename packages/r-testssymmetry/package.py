# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestssymmetry(RPackage):
	"""Tests for Symmetry when the Center of Symmetry is Unknown

	Provides functionality of a statistical testing implementation whether a dataset comes from a symmetric distribution when the center of symmetry is unknown, including Wilcoxon test and sign test procedure. In addition, sample size determination for both tests is provided. The Wilcoxon test procedure is described in Vexler et al. (2023) <https://www.sciencedirect.com/science/article/abs/pii/S0167947323000579>, and the sign test is outlined in Gastwirth (1971) <https://www.jstor.org/stable/2284233>. 
	"""
	
	cran = "TestsSymmetry" 

	version("1.0.0", md5="2bfbf15e1835dede12c895f748c2fcbb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
