# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcotroph(RPackage):
	"""An Implementation of the EcoTroph Ecosystem Modelling Approach

	An approach and software for modelling marine and freshwater ecosystems. It is articulated entirely around trophic levels. EcoTroph's key displays are bivariate plots, with trophic levels as the abscissa, and biomass flows or related quantities as ordinates. Thus, trophic ecosystem functioning can be modelled as a continuous flow of biomass surging up the food web, from lower to higher trophic levels, due to predation and ontogenic processes. Such an approach, wherein species as such disappear, may be viewed as the ultimate stage in the use of the trophic level metric for ecosystem modelling, providing a simplified but potentially useful caricature of ecosystem functioning and impacts of fishing. This version contains catch trophic spectrum analysis (CTSA) function and corrected versions of the mf.diagnosis and create.ETmain functions.
	"""
	
	homepage = "http://sirs.agrocampus-ouest.fr/EcoTroph/"
	cran = "EcoTroph" 

	version("1.6.1", md5="8b37d046f1e5a90e28ef0796eeb660af")

	depends_on("r-xml", type=("build", "run"))
