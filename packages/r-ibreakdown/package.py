# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbreakdown(RPackage):
	"""Model Agnostic Instance Level Variable Attributions

	Model agnostic tool for decomposition of predictions from black boxes.
    Supports additive attributions and attributions with interactions.
    The Break Down Table shows contributions of every variable to a final prediction. 
    The Break Down Plot presents variable contributions in a concise graphical way. 
    This package works for classification and regression models. 
    It is an extension of the 'breakDown' package (Staniak and Biecek 2018) <doi:10.32614/RJ-2018-072>,
    with new and faster strategies for orderings. 
    It supports interactions in explanations and has interactive visuals (implemented with 'D3.js' library). 
    The methodology behind is described in the 'iBreakDown' article (Gosiewska and Biecek 2019) <arXiv:1903.11420>
    This package is a part of the 'DrWhy.AI' universe (Biecek 2018) <arXiv:1806.08915>.
	"""
	
	homepage = "https://ModelOriented.github.io/iBreakDown/"
	cran = "iBreakDown" 

	version("2.1.2", md5="1db5e84db005e7daf9474ea073b23789")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
