# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBroom(RPackage):
	"""Convert Statistical Objects into Tidy Tibbles.

	Summarizes key information about statistical objects in tidy tibbles. This
	makes it easy to report results, create plots and consistently work with
	large numbers of models at once. Broom provides three verbs that each
	provide different types of information about a model. tidy() summarizes
	information about model components such as coefficients of a regression.
	glance() reports information about an entire model, such as goodness of fit
	measures like AIC and BIC. augment() adds information about individual
	observations to a dataset, such as fitted values or influence measures."""

	cran = "broom"

	license("MIT")

	version("1.0.5", md5="d458efb789034fdb8dce79f4a2226850")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-generics@0.0.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
