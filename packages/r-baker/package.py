# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaker(RPackage):
	""""Nested Partially Latent Class Models"

	Provides functions to specify, fit and visualize
    nested partially-latent class models (
    Wu, Deloria-Knoll, Hammitt, and Zeger (2016) <doi:10.1111/rssc.12101>; 
    Wu, Deloria-Knoll, and Zeger (2017) <doi:10.1093/biostatistics/kxw037>;
    Wu and Chen (2021) <doi:10.1002/sim.8804>) for 
    inference of population disease etiology and individual diagnosis. In the motivating
    Pneumonia Etiology Research for Child Health (PERCH) study, because both quantities
    of interest sum to one hundred percent, the PERCH scientists frequently refer to
    them as population etiology pie and individual etiology pie, hence the name of the package.
	"""
	
	homepage = "https://github.com/zhenkewu/baker"
	cran = "baker" 

	version("1.0.3", md5="a287b9a66a5b48450384de0facb539bf")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-r2jags@0.5:", type=("build", "run"))
	depends_on("r-lubridate@1.3:", type=("build", "run"))
	depends_on("r-binom@1.1:", type=("build", "run"))
	depends_on("r-coda@0.16:", type=("build", "run"))
	depends_on("r-robcompositions@2.0.3:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
	depends_on("r-mgcv@1.8.6:", type=("build", "run"))
	depends_on("r-mvbutils@2.7.4.1:", type=("build", "run"))
	depends_on("r-shinyfiles@0.6:", type=("build", "run"))
	depends_on("r-shinydashboard@0.5.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("jags@4.3.2:", type=("build", "link", "run"))
