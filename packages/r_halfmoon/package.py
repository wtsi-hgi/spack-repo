# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHalfmoon(RPackage):
	"""Techniques to Build Better Balance

	Build better balance in causal inference models. 'halfmoon'
    helps you assess propensity score models for balance between groups
    using metrics like standardized mean differences and visualization
    techniques like mirrored histograms. 'halfmoon' supports both
    weighting and matching techniques.
	"""
	
	homepage = "https://github.com/r-causal/halfmoon"
	cran = "halfmoon" 

	version("0.1.0", md5="cca5070410b6a567218557329556b35b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidysmd@0.2:", type=("build", "run"))
