# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredrupdate(RPackage):
	"""Prediction Model Validation and Updating

	Evaluate the predictive performance of an existing (i.e. previously 
    developed) prediction/ prognostic model given relevant information about the 
    existing prediction model (e.g. coefficients) and a new dataset. Provides a 
    range of model updating methods that help tailor the existing model to the 
    new dataset; see Su et al. (2018) <doi:10.1177/0962280215626466>. Techniques 
    to aggregate multiple existing prediction models on the new data are also 
    provided; see Debray et al. (2014) <doi:10.1002/sim.6080> and Martin et al. 
    (2018) <doi:10.1002/sim.7586>).
	"""
	
	homepage = "https://github.com/GlenMartin31/predRupdate"
	cran = "predRupdate" 

	version("0.1.1", md5="43549a509283059e0343249b468e9289")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
