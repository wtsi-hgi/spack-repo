# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtest(RPackage):
	"""Parameter Estimation of Item Response Theory with Estimation of
Latent Distribution

	Item response theory (IRT) parameter estimation using marginal maximum likelihood and expectation-maximization algorithm 
    (Bock & Aitkin, 1981 <doi:10.1007/BF02293801>). 
    Within parameter estimation algorithm, several methods for latent distribution estimation are available.
    Reflecting some features of the true latent distribution, these latent distribution estimation methods can possibly enhance the estimation accuracy and free the normality assumption on the latent distribution.
	"""
	
	homepage = "https://github.com/SeewooLi/IRTest"
	cran = "IRTest" 

	version("2.0.0", md5="f40058ab70c074b3f6d5b8f2912336f8")
	version("1.12.0", md5="e69a20d159eda44459d214db5a3840ce")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-betafunctions", type=("build", "run"))
	depends_on("r-dcurver", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
