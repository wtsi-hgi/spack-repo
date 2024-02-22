# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVbjm(RPackage):
	"""Variational Inference for Joint Model

	The shared random effects joint model is one of the most widely used approaches to study the associations between longitudinal biomarkers and a survival outcome and make dynamic risk predictions using the longitudinally measured biomarkers. 
    One major limitation of joint models is that they could be computationally expensive for complex models where the number of the shared random effects is large.  
    This package can be used to fit complex multivariate joint models using our newly developed algorithm Jieqi Tu and Jiehuan Sun (2023) <doi:10.1002/sim.9619>, which is based on Gaussian variational approximate inference and is computationally efficient.
	"""
	
	cran = "VBJM" 

	version("0.1.0", md5="d43ff7b1b991fa2261fb582104261447")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival@3.2:", type=("build", "run"))
	depends_on("r-statmod@1.4:", type=("build", "run"))
	depends_on("r-pracma@2.2:", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppensmallen", type=("build", "run"))
