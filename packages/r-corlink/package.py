# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorlink(RPackage):
	"""Record Linkage, Incorporating Imputation for Missing Agreement
Patterns, and Modeling Correlation Patterns Between Fields

	A matrix of agreement patterns and counts for record pairs is the input for the procedure.  An EM algorithm is used to impute plausible values for missing record pairs.  A second EM algorithm, incorporating possible correlations between per-field agreement, is used to estimate posterior probabilities that each pair is a true match - i.e. constitutes the same individual.
	"""
	
	cran = "corlink" 

	version("1.0.0", md5="b61145880fe6b7987cfcc9a4cdf8c0e2")

	depends_on("r@3.2.4:", type=("build", "run"))
