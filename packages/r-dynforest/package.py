# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynforest(RPackage):
	"""Random Forest with Multivariate Longitudinal Predictors

	Based on random forest principle, 'DynForest' is able to include 
    multiple longitudinal predictors to provide individual predictions. 
    Longitudinal predictors are modeled through the random forest. The 
    methodology is fully described for a survival outcome in: 
    Devaux, Helmer, Genuer & Proust-Lima (2023) 
    <doi: 10.1177/09622802231206477>.
	"""
	
	homepage = "https://github.com/anthonydevaux/DynForest"
	cran = "DynForest" 

	version("1.1.2", md5="adbfb6acc7fa57c86e5a692ad685b027")
	version("1.1.3", md5="5491ff2641f8081fba3de512ce6fc649")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lcmm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
