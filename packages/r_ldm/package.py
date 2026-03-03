# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdm(RPackage):
	"""Testing Hypotheses About the Microbiome using the Linear
Decomposition Model

	A single analysis path that includes distance-based ordination, global tests of any effect of the microbiome, and tests of the effects of individual taxa with false-discovery-rate (FDR) control. It accommodates both continuous and discrete covariates as well as interaction terms to be tested either singly or in combination, allows for adjustment of confounding covariates, and uses permutation-based p-values that can control for sample correlations. It can be applied to transformed data, and an omnibus test can combine results from analyses conducted on different transformation scales. It can also be used for testing presence-absence associations based on infinite number of rarefaction replicates, testing mediation effects of the microbiome, analyzing censored time-to-event outcomes, and for compositional analysis by fitting linear models to centered-log-ratio taxa count data. 
	"""
	
	homepage = "https://github.com/yijuanhu/LDM"
	cran = "LDM" 

	version("6.0.1", md5="7df8e89e87c7341e1147364454f10346")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gunifrac", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-castor", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
