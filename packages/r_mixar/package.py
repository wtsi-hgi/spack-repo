# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixar(RPackage):
	"""Mixture Autoregressive Models

	Model time series using mixture autoregressive (MAR)
             models.  Implemented are frequentist (EM) and Bayesian
             methods for estimation, prediction and model
             evaluation. See Wong and Li (2002)
             <doi:10.1111/1467-9868.00222>, Boshnakov (2009)
             <doi:10.1016/j.spl.2009.04.009>), and the extensive
             references in the documentation.
	"""
	
	homepage = "https://geobosh.github.io/mixAR/"
	cran = "mixAR" 

	version("0.22.8", md5="fc3a094352879b2123a01454aff5f2ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-gbutils@0.3.1:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
