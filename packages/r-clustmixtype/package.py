# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustmixtype(RPackage):
	"""k-Prototypes Clustering for Mixed Variable-Type Data

	Functions to perform k-prototypes partitioning clustering for
    mixed variable-type data according to Z.Huang (1998): Extensions to the k-Means
    Algorithm for Clustering Large Data Sets with Categorical Variables, Data Mining
    and Knowledge Discovery 2, 283-304.
	"""
	
	cran = "clustMixType" 

	version("0.3-14", md5="81f1956bf601b40f9c18ddf47ac116ed")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
