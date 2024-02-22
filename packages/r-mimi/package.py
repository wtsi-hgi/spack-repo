# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimi(RPackage):
	"""Main Effects and Interactions in Mixed and Incomplete Data

	Generalized low-rank models for mixed and incomplete data frames. The main function may be used for dimensionality reduction of imputation of numeric, binary and count data (simultaneously). Main effects such as column means, group effects, or effects of row-column side information (e.g. user/item attributes in recommendation system) may also be modelled in addition to the low-rank model. Geneviève Robin, Olga Klopp, Julie Josse, Éric Moulines, Robert Tibshirani (2018) <arXiv:1806.09734>.
	"""
	
	cran = "mimi" 

	version("0.2.0", md5="3c86b2f859190a2a43ba4b06db4764bd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
