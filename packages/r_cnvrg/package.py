# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvrg(RPackage):
	"""Dirichlet Multinomial Modeling of Relative Abundance Data

	Implements Dirichlet multinomial modeling of relative abundance data using functionality provided by the 'Stan' software. The purpose of this package is to provide a user friendly way to interface with 'Stan' that is suitable for those new to modeling. For more regarding the modeling mathematics and computational techniques we use see our publication in Molecular Ecology Resources titled 'Dirichlet multinomial modeling outperforms alternatives for analysis of ecological count data' (Harrison et al. 2020 <doi:10.1111/1755-0998.13128>).
	"""
	
	cran = "CNVRG" 

	version("1.0.0", md5="dc37c0e46d6a1d8bdf067b6fd707c684")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
