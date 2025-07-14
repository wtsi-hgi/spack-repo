# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIhw(RPackage):
	"""Independent Hypothesis Weighting

	Independent hypothesis weighting (IHW) is a multiple testing procedure that increases power compared to the method of Benjamini and Hochberg by assigning data-driven weights to each hypothesis. The input to IHW is a two-column table of p-values and covariates. The covariate can be any continuous-valued or categorical variable that is thought to be informative on the statistical properties of each hypothesis test, while it is independent of the p-value under the null hypothesis.
	"""
	
	bioc = "IHW"

	version("1.36.0", commit="f5eb8247d6cc33a2c0fb0ac7bd606f75a76e5eb7")
	version("1.30.0", commit="c97951304bf92d629313a9e88a1321660a2ada72")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-lpsymphony", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
