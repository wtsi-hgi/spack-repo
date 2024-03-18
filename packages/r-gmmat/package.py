# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmmat(RPackage):
	"""Generalized Linear Mixed Model Association Tests

	Perform association tests using generalized linear mixed models (GLMMs) in genome-wide association studies (GWAS) and sequencing association studies. First, GMMAT fits a GLMM with covariate adjustment and random effects to account for population structure and familial or cryptic relatedness. For GWAS, GMMAT performs score tests for each genetic variant as proposed in Chen et al. (2016) <DOI:10.1016/j.ajhg.2016.02.012>. For candidate gene studies, GMMAT can also perform Wald tests to get the effect size estimate for each genetic variant. For rare variant analysis from sequencing association studies, GMMAT performs the variant Set Mixed Model Association Tests (SMMAT) as proposed in Chen et al. (2019) <DOI:10.1016/j.ajhg.2018.12.012>, including the burden test, the sequence kernel association test (SKAT), SKAT-O and an efficient hybrid test of the burden test and SKAT, based on user-defined variant sets.
	"""
	
	cran = "GMMAT" 

	version("1.4.2", md5="79c252d873affb24d6f676dcd43fc6db")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("zstd", type=("build", "link", "run"))
