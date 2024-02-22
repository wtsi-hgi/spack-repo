# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLincom(RPackage):
	"""Linear Biomarker Combination: Empirical Performance Optimization

	Perform two linear combination methods for biomarkers: (1) Empirical performance optimization for specificity (or sensitivity) at a controlled sensitivity (or specificity) level of Huang and Sanda (2022) <doi:10.1214/22-aos2210>, and (2) weighted maximum score estimator with empirical minimization of averaged false positive rate and false negative rate. Both adopt the algorithms of Huang and Sanda (2022) <doi:10.1214/22-aos2210>. 'MOSEK' solver is used and needs to be installed; an academic license for 'MOSEK' is free.
	"""
	
	cran = "lincom" 

	version("1.1", md5="1a0aa25d5d88f960f2695500572747b8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmosek", type=("build", "run"))
