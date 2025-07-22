# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLapmix(RPackage):
	"""Laplace Mixture Model in Microarray Experiments

	Laplace mixture modelling of microarray experiments. A hierarchical Bayesian approach is used, and the hyperparameters are estimated using empirical Bayes. The main purpose is to identify differentially expressed genes.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "lapmix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lapmix_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lapmix/lapmix_1.68.0.tar.gz"]

	version("1.74.0", tag="RELEASE_3_21")
	version("1.68.0", sha256="d43b18bf5c5feec0d7249c59ad342b3cd15f6755f5fad71bcc62dee9249684cf")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
