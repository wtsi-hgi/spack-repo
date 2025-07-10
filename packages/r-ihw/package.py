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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IHW_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IHW/IHW_1.30.0.tar.gz"]

	version("1.30.0", sha256="0b31c7b5794414c546ca255d1e2d0ddc4f56ad8b1a41189b04dceaf4281a3dde")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-lpsymphony", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
