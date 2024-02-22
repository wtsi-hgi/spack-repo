# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKindisperse(RPackage):
	"""Simulate and Estimate Close-Kin Dispersal Kernels

	Functions for simulating and estimating kinship-related dispersal. Based
    on the methods described in M. Jasper, T.L. Schmidt., N.W. Ahmad, S.P. Sinkins & A.A. 
    Hoffmann (2019) <doi:10.1111/1755-0998.13043> "A genomic approach to inferring kinship 
    reveals limited intergenerational dispersal in the yellow fever mosquito".
    Assumes an additive variance model of dispersal in two dimensions, compatible with 
    Wright's neighbourhood area. Simple and composite dispersal simulations are supplied, 
    as well as the functions needed to estimate parent-offspring dispersal for simulated or 
    empirical data, and to undertake sampling design for future field studies of dispersal. 
    For ease of use an integrated Shiny app is also included. 
	"""
	
	homepage = "https://github.com/moshejasper/kindisperse"
	cran = "kindisperse" 

	version("0.10.2", md5="5e3ef73c9fba7ca35ea2716888c0699b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
