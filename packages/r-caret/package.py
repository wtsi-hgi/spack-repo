# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaret(RPackage):
	"""Classification and Regression Training.

	Misc functions for training and plotting classification and regression
	models."""

	cran = "caret"

	version("6.0-94", md5="5f4c1945b20e632187f5534a59a12c8c")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice@0.20:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-modelmetrics@1.2.2.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-recipes@0.1.10:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-withr@2:", type=("build", "run"))
