# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreta(RPackage):
	"""Simple and Scalable Statistical Modelling in R

	Write statistical models in R and fit them by MCMC and
    optimisation on CPUs and GPUs, using Google 'TensorFlow'.  greta lets
    you write your own model like in BUGS, JAGS and Stan, except that you
    write models right in R, it scales well to massive datasets, and it’s
    easy to extend and build on.  See the website for more information,
    including tutorials, examples, package documentation, and the greta
    forum.
	"""
	
	homepage = "https://greta-stats.org"
	cran = "greta" 

	version("0.4.4", md5="8c934c15002c2fee781eac7b6e4c8e78")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-future@1.22.1:", type=("build", "run"))
	depends_on("r-glue@1.5.1:", type=("build", "run"))
	depends_on("r-parallelly@1.29:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reticulate@1.19:", type=("build", "run"))
	depends_on("r-tensorflow@2.7:", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
	depends_on("python@2.7.0:", type=("build", "link", "run"))
	depends_on("py-tensorflow@1.14:", type=("build", "link", "run"))
	depends_on("py-tensorflow-probability", type=("build", "link", "run"))
