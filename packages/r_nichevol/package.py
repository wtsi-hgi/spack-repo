# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNichevol(RPackage):
	"""Tools for Ecological Niche Evolution Assessment Considering
Uncertainty

	A collection of tools that allow users to perform critical steps 
    in the process of assessing ecological niche evolution over phylogenies, with
    uncertainty incorporated explicitly in reconstructions. The method proposed
    here for ancestral reconstruction of ecological niches characterizes species'
    niches using a bin-based approach that incorporates uncertainty in estimations.
    Compared to other existing methods, the approaches presented here reduce risk
    of overestimation of amounts and rates of ecological niche evolution. The
    main analyses include: initial exploration of environmental data in occurrence
    records and accessible areas, preparation of data for phylogenetic analyses,
    executing comparative phylogenetic analyses of ecological niches, and plotting
    for interpretations. Details on the theoretical background and methods used 
    can be found in: Owens et al. (2020) <doi:10.1002/ece3.6359>,
    Peterson et al. (1999) <doi:10.1126/science.285.5431.1265>,
    Soberón and Peterson (2005) <doi:10.17161/bi.v2i0.4>,
    Peterson (2011) <doi:10.1111/j.1365-2699.2010.02456.x>,
    Barve et al. (2011) <doi:10.1111/ecog.02671>, 
    Machado-Stredel et al. (2021) <doi:10.21425/F5FBG48814>,
    Owens et al. (2013) <doi:10.1016/j.ecolmodel.2013.04.011>, 
    Saupe et al. (2018) <doi:10.1093/sysbio/syx084>, and 
    Cobos et al. (2021) <doi:10.1111/jav.02868>.
	"""
	
	homepage = "https://github.com/marlonecobos/nichevol"
	cran = "nichevol" 

	version("0.1.20", md5="564a2c0a9c1ca52f9c13a1924c8d8279")

	depends_on("r-ape@5.3:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-castor@1.4:", type=("build", "run"))
	depends_on("r-geiger@2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-terra@1.6:", type=("build", "run"))
