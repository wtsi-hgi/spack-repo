# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStemanalysis(RPackage):
	"""Reconstructing Tree Growth and Carbon Accumulation with Stem
Analysis Data

	Use stem analysis data to reconstructing tree growth and carbon accumulation. Users can independently or in combination perform a number of standard tasks for any tree species.
    (i) Age class determination.
    (ii) The cumulative growth, mean annual increment, and current annual increment of diameter at breast height (DBH) with bark, tree height, and stem volume with bark are estimated. 
    (iii) Tree biomass and carbon storage estimation from volume and allometric models are calculated. 
    (iv) Height-diameter relationship is fitted with nonlinear models, if diameter at breast height (DBH) or tree height are available, which can be used to retrieve tree height and diameter at breast height (DBH).
    <https://github.com/forestscientist/StemAnalysis>.
	"""
	
	homepage = "https://github.com/forestscientist/StemAnalysis"
	cran = "StemAnalysis" 

	version("0.1.0", md5="55cc76cb6f41d9ba4d79f9d0a4e9ffa3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lmfor@1:", type=("build", "run"))
