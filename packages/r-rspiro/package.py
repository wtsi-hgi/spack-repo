# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspiro(RPackage):
	"""Implementation of Spirometry Equations

	Implementation of various spirometry equations
    in R, currently the GLI-2012 (Global Lung Initiative;
    Quanjer et al. 2012 <doi:10.1183/09031936.00080312>),
    the race-neutral GLI global 2022 (Global Lung Initiative;
    Bowerman et al. 2023 <doi:10.1164/rccm.202205-0963OC>) and the
    NHANES3 (National Health and Nutrition Examination Survey;
    Hankinson et al. 1999 <doi:10.1164/ajrccm.159.1.9712108>)
    equations. 
    Contains user-friendly functions to calculate predicted 
    and LLN (Lower Limit of Normal) values for different 
    spirometric parameters such as FEV1 (Forced Expiratory 
    Volume in 1 second), FVC (Forced Vital Capacity), etc, 
    and to convert absolute spirometry measurements 
    to percent (%) predicted and z-scores.
	"""
	
	cran = "rspiro" 

	version("0.4", md5="1562dc025e13d3cdc4c90a2bd3f4db71")

	depends_on("r@2.10:", type=("build", "run"))
