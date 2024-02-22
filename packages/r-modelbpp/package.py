# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelbpp(RPackage):
	"""Model BIC Posterior Probability

	Fits the neighboring models of a fitted
  structural equation model and assesses the model
  uncertainty of the fitted model based on BIC posterior
  probabilities, using the method presented in
  Wu, Cheung, and Leung (2020)
  <doi:10.1080/00273171.2019.1574546>.
	"""
	
	homepage = "https://sfcheung.github.io/modelbpp/"
	cran = "modelbpp" 

	version("0.1.3", md5="563faf5a564872aa39e657726136fdd9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
