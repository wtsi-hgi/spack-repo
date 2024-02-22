# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimblescr(RPackage):
	"""Spatial Capture-Recapture (SCR) Methods Using 'nimble'

	Provides utility functions, distributions, and fitting methods for Bayesian Spatial Capture-Recapture (SCR) and Open Population Spatial Capture-Recapture (OPSCR) modelling using the nimble package (de Valpine et al. 2017 <doi:10.1080/10618600.2016.1172487 >). Development of the package was motivated primarily by the need for flexible and efficient analysis of large-scale SCR data (Bischof et al. 2020 <doi:10.1073/pnas.2011383117 >). Computational methods and techniques implemented in nimbleSCR include those discussed in Turek et al. 2021 <doi:10.1002/ecs2.3385>; among others. For a recent application of nimbleSCR, see Milleret et al. (2021) <doi:10.1098/rsbl.2021.0128>.
	"""
	
	cran = "nimbleSCR" 

	version("0.2.1", md5="653ad26f2e95c7a23771c34ad260d352")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
