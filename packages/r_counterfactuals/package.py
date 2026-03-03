# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCounterfactuals(RPackage):
	"""Counterfactual Explanations

	Modular and unified R6-based interface for counterfactual explanation methods.
    The following methods are currently implemented: Burghmans et al. (2022) <arXiv:2104.07411>, 
    Dandl et al. (2020) <doi:10.1007/978-3-030-58112-1_31> and Wexler et al. (2019) <doi:10.1109/TVCG.2019.2934619>.
    Optional extensions allow these methods to be applied to a variety of models and use cases.
    Once generated, the counterfactuals can be analyzed and visualized by provided functionalities.
	"""
	
	homepage = "https://github.com/dandls/counterfactuals"
	cran = "counterfactuals" 

	version("0.1.2", md5="2911e607c8e8509d1eeef9248516624f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
	depends_on("r-iml", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-miesmuschel", type=("build", "run"))
	depends_on("r-bbotk", type=("build", "run"))
