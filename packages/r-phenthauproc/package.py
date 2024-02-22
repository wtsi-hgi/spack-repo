# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenthauproc(RPackage):
	"""Phenology Modelling of Thaumetopoea Processionea

	Methods to calculate and present 'PHENTHAUproc', an early warning and decision support system for hazard assessment and control of oak processionary moth (OPM) using local and spatial temperature data. It was created by Halbig et al. 2024 (<doi:10.1016/j.foreco.2023.121525>) at FVA (<https://www.fva-bw.de/en/homepage/>) Forest Research Institute Baden-Wuerttemberg, Germany and at BOKU - University of Natural Ressources and Life Sciences, Vienna, Austria.
	"""
	
	cran = "PHENTHAUproc" 

	version("1.0.1", md5="08e52566692dd92eedd4ea5e395b6520")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate@1.9:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-terra@1.7:", type=("build", "run"))
