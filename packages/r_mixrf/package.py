# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixrf(RPackage):
	"""A Random-Forest-Based Approach for Imputing Clustered Incomplete
Data

	It offers random-forest-based functions to impute clustered
    incomplete data. The package is tailored for but not limited to imputing
    multitissue expression data, in which a gene's expression is measured on the
    collected tissues of an individual but missing on the uncollected tissues.
	"""
	
	homepage = "https://github.com/randel/MixRF"
	cran = "MixRF" 

	version("1.0", md5="6038fbdc7305bab320e673311fa419fe")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
