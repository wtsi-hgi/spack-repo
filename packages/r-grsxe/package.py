# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrsxe(RPackage):
	"""Testing Gene-Environment Interactions Through Genetic Risk
Scores

	Statistical testing procedures for detecting
  GxE (gene-environment) interactions. The main focus lies on
  GRSxE interaction tests that aim at detecting GxE interactions
  through GRS (genetic risk scores). Moreover, a novel testing
  procedure based on bagging and OOB (out-of-bag) predictions is
  implemented for incorporating all available observations at
  both GRS construction and GxE testing (Lau et al., 2023,
  <doi:10.1038/s41598-023-28172-4>).
	"""
	
	cran = "GRSxE" 

	version("1.0.1", md5="d567fa581f7cba2173bfc6fd29365715")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
