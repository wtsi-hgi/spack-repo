# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayespm(RPackage):
	"""Bayesian Statistical Process Monitoring

	The R-package bayespm implements Bayesian Statistical Process Control and Monitoring (SPC/M) methodology. These methods utilize available prior information and/or historical data, providing efficient online quality monitoring of a process, in terms of identifying moderate/large transient shifts (i.e., outliers) or persistent shifts of medium/small size in the process. These self-starting, sequentially updated tools can also run under complete absence of any prior information. The Predictive Control Charts (PCC) are introduced for the quality monitoring of data from any discrete or continuous distribution that is a member of the regular exponential family. The Predictive Ratio CUSUMs (PRC) are introduced for the Binomial, Poisson and Normal data (a later version of the library will cover all the remaining distributions from the regular exponential family). The PCC targets transient process shifts of typically large size (a.k.a. outliers), while PRC is focused in detecting persistent (structural) shifts that might be of medium or even small size. Apart from monitoring, both PCC and PRC provide the sequentially updated posterior inference for the monitored parameter. Bourazas K., Kiagias D. and Tsiamyrtzis P. (2022) "Predictive Control Charts (PCC): A Bayesian approach in online monitoring of short runs" <doi:10.1080/00224065.2021.1916413>, Bourazas K., Sobas F. and Tsiamyrtzis, P. 2023. "Predictive ratio CUSUM (PRC): A Bayesian approach in online change point detection of short runs" <doi:10.1080/00224065.2022.2161434>, Bourazas K., Sobas F. and Tsiamyrtzis, P. 2023. "Design and properties of the predictive ratio cusum (PRC) control charts" <doi:10.1080/00224065.2022.2161435>. 
	"""
	
	cran = "bayespm" 

	version("0.2.0", md5="84b73c68033f304bd71eba5e724fd8a6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
