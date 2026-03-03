# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenesse(RPackage):
	"""Estimate Phenological Metrics using Presence-Only Data

	Generates Weibull-parameterized estimates of phenology for any percentile of 
    a distribution using the framework established in Cooke (1979)
    <doi:10.1093/biomet/66.2.367>. Extensive testing against other 
    estimators suggest the weib_percentile() function is especially useful in 
    generating more accurate and less biased estimates of onset and offset 
    (Belitz et al. 2020 <doi.org:10.1111/2041-210X.13448>. Non-parametric 
    bootstrapping can be used to generate confidence intervals around those 
    estimates, although this is computationally expensive. Additionally, this 
    package offers an easy way to perform non-parametric bootstrapping to 
    generate confidence intervals for quantile estimates, mean estimates, 
    or any statistical function of interest.
	"""
	
	homepage = "https://github.com/mbelitz/phenesse"
	cran = "phenesse" 

	version("0.1.2", md5="ff53a70ee6712ffec27cf4709e6ec52c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
