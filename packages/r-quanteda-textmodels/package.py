# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantedaTextmodels(RPackage):
	"""Scaling Models and Classifiers for Textual Data

	Scaling models and classifiers for sparse matrix objects representing 
    textual data in the form of a document-feature matrix.  Includes original 
    implementations of 'Laver', 'Benoit', and Garry's (2003) <doi:10.1017/S0003055403000698>,
    'Wordscores' model, the Perry and 'Benoit' (2017) <arXiv:1710.08963> class affinity scaling model, 
    and the 'Slapin' and 'Proksch' (2008) <doi:10.1111/j.1540-5907.2008.00338.x> 'wordfish'
    model, as well as methods for correspondence analysis, latent semantic analysis,
    and fast Naive Bayes and linear 'SVMs' specially designed for sparse textual data.
	"""
	
	homepage = "https://github.com/quanteda/quanteda.textmodels"
	cran = "quanteda.textmodels" 

	version("0.9.6", md5="a5e35f9e4d12b431be48175a6283f328")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-liblinear", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
