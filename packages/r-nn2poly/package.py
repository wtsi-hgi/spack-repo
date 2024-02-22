# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNn2poly(RPackage):
	"""Neural Network Weights Transformation into Polynomial
Coefficients

	Implements a method that builds the coefficients of a polynomial
    model that performs almost equivalently as a given neural network
    (densely connected). This is achieved using Taylor expansion at the
    activation functions.  The obtained polynomial coefficients can be used
    to explain features (and their interactions) importance  in the neural network,
    therefore working as a tool for interpretability or eXplainable Artificial 
    Intelligence (XAI). See Morala et al. 2021 <doi:10.1016/j.neunet.2021.04.036>,
    and 2023 <doi:10.1109/TNNLS.2023.3330328>.
	"""
	
	homepage = "https://ibidat.github.io/nn2poly/"
	cran = "nn2poly" 

	version("0.1.1", md5="911106807f344b5819c06bd010dc75be")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
