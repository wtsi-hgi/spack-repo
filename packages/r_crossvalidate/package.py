# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossvalidate(RPackage):
	"""Classes and Methods for Cross Validation of "Class Prediction"
Algorithms

	Defines classes and methods to cross-validate various
  binary classification algorithms used for "class prediction"
  problems.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org"
	cran = "CrossValidate" 

	version("2.3.4", md5="fe62e5163d5c84199011e7bf7475686f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-modeler", type=("build", "run"))
	depends_on("r-oompabase@3.0.1:", type=("build", "run"))
