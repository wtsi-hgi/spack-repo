# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClvtools(RPackage):
	"""Tools for Customer Lifetime Value Estimation

	
    A set of state-of-the-art probabilistic modeling approaches to derive estimates of individual customer lifetime values (CLV).
    Commonly, probabilistic approaches focus on modelling 3 processes, i.e. individuals' attrition, transaction, and spending process. 
    Latent customer attrition models, which are also known as "buy-'til-you-die models", model the attrition as well as the transaction process. 
    They are used to make inferences and predictions about transactional patterns of individual customers such as their future purchase behavior. 
    Moreover, these models have also been used to predict individuals’ long-term engagement in activities such as playing an online game or 
    posting to a social media platform. The spending process is usually modelled by a separate probabilistic model. Combining these results yields in 
    lifetime values estimates for individual customers.
    This package includes fast and accurate implementations of various probabilistic models for non-contractual settings 
    (e.g., grocery purchases or hotel visits). All implementations support time-invariant covariates, which can be used to control for e.g., 
    socio-demographics. If such an extension has been proposed in literature, we further provide the possibility to control for time-varying 
    covariates to control for e.g., seasonal patterns. 
    Currently, the package includes the following latent attrition models to model individuals' attrition and transaction process: 
    [1] Pareto/NBD model (Pareto/Negative-Binomial-Distribution), 
    [2] the Extended Pareto/NBD model (Pareto/Negative-Binomial-Distribution with time-varying covariates), 
    [3] the BG/NBD model (Beta-Gamma/Negative-Binomial-Distribution) and the 
    [4] GGom/NBD (Gamma-Gompertz/Negative-Binomial-Distribution). 
    Further, we provide an implementation of the Gamma/Gamma model to model the spending process of individuals.
	"""
	
	homepage = "https://github.com/bachmannpatrick/CLVTools"
	cran = "CLVTools" 

	version("0.10.0", md5="450c9252ae1f5fa331acf4b573ebd3ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-formula@1.2.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.8:", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-optimx@2019.12.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.500.2:", type=("build", "run"))
	depends_on("r-rcppgsl@0.3.7:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
