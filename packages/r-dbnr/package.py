# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbnr(RPackage):
	"""Dynamic Bayesian Network Learning and Inference

	Learning and inference over dynamic Bayesian networks of arbitrary 
    Markovian order. Extends some of the functionality offered by the 'bnlearn' 
    package to learn the networks from data and perform exact inference. 
    It offers three structure learning algorithms for dynamic Bayesian networks:
    Trabelsi G. (2013) <doi:10.1007/978-3-642-41398-8_34>, Santos F.P. and Maciel C.D. (2014)
    <doi:10.1109/BRC.2014.6880957>, Quesada D., Bielza C. and Larrañaga P. (2021)
    <doi:10.1007/978-3-030-86271-8_14>. It also offers the possibility to perform 
    forecasts of arbitrary length. A tool for visualizing the structure of the 
    net is also provided via the 'visNetwork' package.
	"""
	
	homepage = "https://github.com/dkesada/dbnR"
	cran = "dbnR" 

	version("0.7.8", md5="519a0d65ac70a0ca531909b21329886b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bnlearn@4.5:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-mass@7.3.55:", type=("build", "run"))
