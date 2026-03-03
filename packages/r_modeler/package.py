# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeler(RPackage):
	"""Classes and Methods for Training and Using Binary Prediction
Models

	Defines classes and methods to learn models and use them
  to predict binary outcomes.  These are generic tools, but we also
  include specific examples for many common classifiers.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "Modeler" 

	version("3.4.5", md5="1cd85f38941e505a8ce3e181688abc37")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-classdiscovery", type=("build", "run"))
	depends_on("r-classcomparison", type=("build", "run"))
	depends_on("r-oompabase", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-tailrank", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
