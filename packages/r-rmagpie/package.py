# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmagpie(RPackage):
	"""MicroArray Gene-expression-based Program In Error rate estimation

	Microarray Classification is designed for both biologists and statisticians. It offers the ability to train a classifier on a labelled microarray dataset and to then use that classifier to predict the class of new observations. A range of modern classifiers are available, including support vector machines (SVMs), nearest shrunken centroids (NSCs)... Advanced methods are provided to estimate the predictive error rate and to report the subset of genes which appear essential in discriminating between classes.
	"""
	
	homepage = "http://www.bioconductor.org/"
	bioc = "Rmagpie" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rmagpie_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rmagpie/Rmagpie_1.58.0.tar.gz"]

	version("1.64.0", tag="RELEASE_3_21")
	version("1.58.0", sha256="a2e5bd407cf26c48fa91d3569621d539a704820784dded4978655d26d690a57c")

	depends_on("r@2.6.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
