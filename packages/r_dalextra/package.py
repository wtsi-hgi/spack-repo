# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDalextra(RPackage):
	"""Extension for 'DALEX' Package

	Provides wrapper of various machine learning models. 
  In applied machine learning, there 
  is a strong belief that we need to strike a balance 
  between interpretability and accuracy. 
  However, in field of the interpretable machine learning, 
  there are more and more new ideas for explaining black-box models, 
  that are implemented in 'R'. 
  'DALEXtra' creates 'DALEX' Biecek (2018) <arXiv:1806.08915> explainer for many type of models
  including those created using 'python' 'scikit-learn' and 'keras' libraries, and 'java' 'h2o' library. 
  Important part of the package is Champion-Challenger analysis and innovative approach
  to model performance across subsets of test data presented in Funnel Plot. 
	"""
	
	homepage = "https://ModelOriented.github.io/DALEXtra/"
	cran = "DALEXtra" 

	version("2.3.0", md5="38f865e9b2c5a38df41061af63098fb9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dalex@2.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
