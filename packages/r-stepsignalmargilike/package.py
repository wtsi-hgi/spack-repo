# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepsignalmargilike(RPackage):
	"""Step-Wise Signal Extraction via Marginal Likelihood

	Provides function to estimate multiple change points
    using marginal likelihood method. See the Manual file in data folder for
    a detailed description of all functions, and a walk through tutorial.
    For more information of the method, please see Du, Kao and Kou (2016) 
    <doi:10.1080/01621459.2015.1006365>.
	"""
	
	cran = "StepSignalMargiLike" 

	version("2.6.0", md5="a4aecb49ee6eb8849b00ac420d49d16e")

	depends_on("r-rcpp", type=("build", "run"))
