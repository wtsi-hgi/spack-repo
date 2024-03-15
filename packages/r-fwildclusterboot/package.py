# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFwildclusterboot(RPackage):
	"""Fast Wild Cluster Bootstrap Inference for Linear Models

	Implementation of fast algorithms for wild cluster bootstrap 
             inference developed in 'Roodman et al' (2019, 'STATA' Journal,
             <doi:10.1177/1536867X19830877>) and 'MacKinnon et al' (2022), 
             which makes it feasible to quickly calculate bootstrap test 
             statistics based on a large number of bootstrap draws even for 
             large samples. Multiple bootstrap types as described in 'MacKinnon, 
             Nielsen & Webb' (2022) are supported. 
             Further, 'multiway' clustering, regression weights, 
             bootstrap weights, fixed effects and 'subcluster' bootstrapping
             are supported. Further, both restricted ('WCR') and unrestricted
             ('WCU') bootstrap are supported. Methods are provided for a variety 
             of fitted models, including 'lm()', 'feols()' 
             (from package 'fixest') and 'felm()' (from package 'lfe'). 
             Additionally implements a 'heteroskedasticity-robust' ('HC1') wild 
             bootstrap.
             Last, the package provides an R binding to 'WildBootTests.jl',
             which provides additional speed gains and functionality, 
             including the 'WRE' bootstrap for instrumental variable models 
             (based on models of type 'ivreg()' from package 'ivreg')
             and hypotheses with q > 1.
	"""
	
	homepage = "https://s3alfisc.github.io/fwildclusterboot/"
	cran = "fwildclusterboot" 

	version("0.13.0", md5="8c8d7ddda6edde52f3f5f5c0f9f2705d")

	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-dreamerr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-juliaconnector", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summclust", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("julia", type=("build", "link", "run"))
