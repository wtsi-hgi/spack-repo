# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHlt(RPackage):
	"""Higher-Order Item Response Theory

	Higher-order latent trait theory (item response theory). We
    implement the generalized partial credit model with a second-order latent
    trait structure. Latent regression can be done on the second-order latent
    trait. For a pre-print of the methods,
    see, "Latent Regression in Higher-Order Item Response Theory with the R
    Package hlt" <https://mkleinsa.github.io/doc/hlt_proof_draft_brmic.pdf>.
	"""
	
	homepage = "https://github.com/mkleinsa/hlt"
	cran = "hlt" 

	version("1.3.1", md5="75e01ff497b78a4896189ef07447cd58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
