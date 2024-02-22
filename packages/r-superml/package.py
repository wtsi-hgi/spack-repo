# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperml(RPackage):
	"""Build Machine Learning Models Like Using Python's Scikit-Learn
Library in R

	The idea is to provide a standard interface 
             to users who use both R and Python for building machine learning models. 
             This package provides a scikit-learn's fit, predict interface to 
             train machine learning models in R.    
	"""
	
	homepage = "https://github.com/saraswatmks/superml"
	cran = "superml" 

	version("0.5.7", md5="1e68466a24598b4d4dde197f77793248")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-metrics@0.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
