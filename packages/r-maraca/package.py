# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaraca(RPackage):
	"""The Maraca Plot: Visualization of Hierarchical Composite
Endpoints in Clinical Trials

	Library that supports visual interpretation of hierarchical composite
    endpoints (HCEs). HCEs are complex constructs used as primary endpoints in
    clinical trials, combining outcomes of different types into ordinal endpoints,
    in which each patient contributes the most clinically important event (one and
    only one) to the analysis. See Karpefors M et al. (2022)
    <doi:10.1177/17407745221134949>.
	"""
	
	homepage = "https://github.com/AstraZeneca/maraca"
	cran = "maraca" 

	version("0.6", md5="6a234ef99601d9f27aab8298b9853f98")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hce@0.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
