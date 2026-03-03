# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmc(RPackage):
	"""High Dimensional Mean Comparison with Projection and
Cross-Fitting

	Provides interpretable High-dimensional Mean Comparison methods (HMC). For example, users can use them to assess the difference in gene expression between two treatment groups. It is not a gene-by-gene comparison. Instead, we focus on the interplay between features and are interested in those that are predictive of the group label. The methods are valid frequentist tests and give sparse estimates indicating which features contribute to the test results.
	"""
	
	cran = "HMC" 

	version("1.0", md5="7088035ad5eb0f237717844ed147391d")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
