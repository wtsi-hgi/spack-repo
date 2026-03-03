# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStelfi(RPackage):
	"""Hawkes and Log-Gaussian Cox Point Processes Using Template Model
Builder

	Fit Hawkes and log-Gaussian Cox process models with extensions. Introduced in Hawkes (1971) <doi:10.2307/2334319> a Hawkes process is a self-exciting temporal point process where the occurrence of an event immediately increases the chance of another. We extend this to consider self-inhibiting process and a non-homogeneous background rate. A log-Gaussian Cox process is a Poisson point process where the log-intensity is given by a Gaussian random field. We extend this  to a joint likelihood formulation fitting a marked log-Gaussian Cox model. In addition, the package offers functionality to fit self-exciting spatiotemporal point processes. Models are fitted via maximum likelihood using 'TMB' (Template Model Builder). Where included 1) random fields are assumed to be Gaussian and are integrated over using the Laplace approximation and 2) a stochastic partial differential equation model, introduced by Lindgren, Rue, and Lindström. (2011) <doi:10.1111/j.1467-9868.2011.00777.x>, is defined for the field(s). 
	"""
	
	homepage = "https://github.com/cmjt/stelfi/"
	cran = "stelfi" 

	version("1.0.1", md5="466d07899d61d95a3a100d4c2bf7007f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-fmesher", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2@3.4.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
