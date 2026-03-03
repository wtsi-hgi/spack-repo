# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulasim(RPackage):
	"""Virtual Patient Simulation by Copula Invariance Property

	To optimize clinical trial designs and data analysis methods consistently through trial simulation, we need to simulate multivariate mixed-type virtual patient data independent of designs and analysis methods under evaluation. To make the outcome of optimization more realistic, relevant empirical patient level data should be utilized when it’s available. However, a few problems arise in simulating trials based on small empirical data, where the underlying marginal distributions and their dependence structure cannot be understood or verified thoroughly due to the limited sample size. To resolve this issue, we use the copula invariance property, which can generate the joint distribution without making a strong parametric assumption. The function copula.sim can generate virtual patient data with optional data validation methods that are based on energy distance and ball divergence measurement. The function compare.copula.sim can conduct comparison of marginal mean and covariance of simulated data. To simulate patient-level data from a hypothetical treatment arm that would perform differently from the observed data, the function new.arm.copula.sim can be used to generate new multivariate data with the same dependence structure of the original data but with a shifted mean vector.
	"""
	
	homepage = "https://github.com/psyen0824/copulaSim"
	cran = "copulaSim" 

	version("0.0.1", md5="4b03a12729326dd51e9c9198c5ba9f3a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.12:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
