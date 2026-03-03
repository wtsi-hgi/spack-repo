# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiometryassist(RPackage):
	"""Functions to Assist Design and Analysis of Agronomic Experiments

	Provides functions to aid in the design and analysis of
    agronomic and agricultural experiments through easy access to
    documentation and helper functions, especially for users who are
    learning these concepts. While not required for most functionality,
    this package enhances the `asreml` package which provides a 
    computationally efficient algorithm for fitting mixed models 
    using Residual Maximum Likelihood. It is a commercial package 
    that can be purchased as 'asreml-R' from 'VSNi' 
    <https://vsni.co.uk/>, who will supply a zip file for local 
    installation/updating (see <https://asreml.kb.vsni.co.uk/>). 
	"""
	
	homepage = "https://biometryhub.github.io/biometryassist/"
	cran = "biometryassist" 

	version("1.1.3", md5="6f59244c2bd1f04fad958481f09b0df7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
