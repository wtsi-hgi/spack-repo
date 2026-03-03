# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgmrfmix(RPackage):
	"""Sparse Gaussian Markov Random Field Mixtures for Anomaly
Detection

	An implementation of sparse Gaussian Markov random field mixtures 
  presented by Ide et al. (2016) <doi:10.1109/ICDM.2016.0119>.
  It provides a novel anomaly detection method for multivariate noisy sensor data.
  It can automatically handle multiple operational modes.
  And it can also compute variable-wise anomaly scores.
	"""
	
	cran = "sGMRFmix" 

	version("0.3.0", md5="1dec2ce835db75d60fd8fcd43f5c7ecf")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
