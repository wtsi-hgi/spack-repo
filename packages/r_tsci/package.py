# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsci(RPackage):
	"""Tools for Causal Inference with Possibly Invalid Instrumental
Variables

	Two stage curvature identification with machine learning for causal 
    inference in settings when instrumental variable regression is not suitable
    because of potentially invalid instrumental variables. Based on Guo and 
    Buehlmann (2022) "Two Stage Curvature Identification with Machine Learning: 
    Causal Inference with Possibly Invalid Instrumental Variables"
    <arXiv:2203.12808>. The vignette is available in Carl, Emmenegger, Bühlmann and Guo (2023) 
    "TSCI: two stage curvature identification for causal inference with 
    invalid instruments" <arXiv:2304.00513>.
	"""
	
	homepage = "https://github.com/dlcarl/TSCI"
	cran = "TSCI" 

	version("3.0.4", md5="a01fc35a1af740d057fbeed90aef732d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
