# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedmem(RPackage):
	"""Tools for Discrete Multivariate Mixed Membership Models

	Fits mixed membership models with discrete multivariate data (with
    or without repeated measures) following the general framework of Erosheva et al
    (2004). This package uses a Variational EM approach by approximating the
    posterior distribution of latent memberships and selecting hyperparameters
    through a pseudo-MLE procedure. Currently supported data types are
    Bernoulli, multinomial and rank (Plackett-Luce). The extended GoM model with 
    fixed stayers from Erosheva et al (2007) is now also supported. See Airoldi et al 
    (2014) for other examples of mixed membership models.
	"""
	
	cran = "mixedMem" 

	version("1.1.2", md5="05d3cde9b39718822424e2063c8b5c0f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.11.3:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
