# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVicc(RPackage):
	"""Varying Intraclass Correlation Coefficients

	Compute group-specific intraclass correlation coefficients, 
    Bayesian testing of homogenous within-group variance, and spike-and-slab
    model selection to determine which groups share a common within-group 
    variance in a one-way random effects model <10.31234/osf.io/hpq7w>.
	"""
	
	cran = "vICC" 

	version("1.0.0", md5="faafd261585c1fb4441c3cf358970c4b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-coda@0.19.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rdpack@0.11.1:", type=("build", "run"))
	depends_on("r-rjags@4.10:", type=("build", "run"))
