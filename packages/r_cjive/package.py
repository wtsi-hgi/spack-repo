# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCjive(RPackage):
	"""Canonical Joint and Individual Variation Explained (CJIVE)

	Joint and Individual Variation Explained (JIVE) is a method for decomposing multiple datasets obtained on the same subjects into
		shared structure, structure unique to each dataset, and noise. The two most common implementations are R.JIVE, an iterative
		approach, and AJIVE, which uses principal angle analysis. JIVE estimates subspaces but interpreting these subspaces can be
		challenging with AJIVE or R.JIVE. We expand upon insights into AJIVE as a canonical correlation analysis (CCA) of principal component
		scores. This reformulation, which we call CJIVE, 1) provides an ordering of joint components by the degree of correlation between
		corresponding canonical variables; 2) uses a computationally efficient permutation test for the number of joint components, which
		provides a p-value for each component; and 3) can be used to predict subject scores for out-of-sample observations.
		Please cite the following article when utilizing this package: 
		Murden, R., Zhang, Z., Guo, Y., & Risk, B. (2022) <doi:10.3389/fnins.2022.969510>.
	"""
	
	cran = "CJIVE" 

	version("0.1.0", md5="bc5f372564dd8765978e1b435d452d5b")

	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
