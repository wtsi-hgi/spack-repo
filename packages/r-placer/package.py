# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlacer(RPackage):
	"""PLastic ACcumulation Estimate using R (PLACER)

	Assessment of the prevalence of plastic
    debris in bird nests based on bootstrap replicates. The package allows for 
    calculating bootstrapped 95% confidence intervals for the estimated prevalence 
    of debris. Combined with a Bayesian approach, the resampling simulations can 
    be also used to define appropriate sample sizes to detect prevalence of plastics. 
    The method has wide application, and can also be applied to estimate confidence 
    intervals and define sample sizes for the prevalence of plastics ingested by any 
    other organisms. The method is described in Tavares et al. (Submitted). 
	"""
	
	cran = "placer" 

	version("0.1.3", md5="04a1878ce28a3373bbe3264be663a1f9")

	depends_on("r@3.5:", type=("build", "run"))
