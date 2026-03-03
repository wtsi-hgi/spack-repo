# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfprobability(RPackage):
	"""Interface to 'TensorFlow Probability'

	Interface to 'TensorFlow Probability', a 'Python' library built on 'TensorFlow'
    that makes it easy to combine probabilistic models and deep learning on modern hardware ('TPU', 'GPU').
    'TensorFlow Probability' includes a wide selection of probability distributions and bijectors, probabilistic layers,
    variational inference, Markov chain Monte Carlo, and optimizers such as Nelder-Mead, BFGS, and SGLD.
	"""
	
	homepage = "https://github.com/rstudio/tfprobability"
	cran = "tfprobability" 

	version("0.15.1", md5="aef56a13c869fa71e4f35d0b6cefbabd")

	depends_on("r-tensorflow@2.4:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("py-tensorflow-probability", type=("build", "link", "run"))
