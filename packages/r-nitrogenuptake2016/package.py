# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNitrogenuptake2016(RPackage):
	"""Data and Source Code From: Nitrogen Uptake and Allocation
Estimates for Spartina Alterniflora and Distichlis Spicata

	Contains data, code, and figures from Hill et al. 2018a (Journal of Experimental Marine Biology and Ecology; <DOI: 10.1016/j.jembe.2018.07.006>) and Hill et al. 2018b (Data In Brief <DOI: 10.1016/j.dib.2018.09.133>). Datasets document plant allometry, stem heights, nutrient and stable isotope content, and sediment denitrification enzyme assays. The data and analysis offer an examination of nitrogen uptake and allocation in two salt marsh plant species.
	"""
	
	homepage = "https://github.com/troyhill/NitrogenUptake2016"
	cran = "NitrogenUptake2016" 

	version("0.2.3", md5="8925e457e5facd020d9a96cac9f18601", url="https://cran.r-project.org/src/contrib/NitrogenUptake2016_0.2.3.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
