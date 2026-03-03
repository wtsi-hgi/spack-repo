# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariskscore(RPackage):
	"""VA CVD Risk Score

	Estimates the predicted 10-year cardiovascular (CVD) risk score (in probability) for women military service 
    members and veterans by inputting patient profiles. The proposed women CVD risk score improves the accuracy of the 
    existing American College of Cardiology/American Heart Association CVD risk assessment
    tool in predicting long‐term CVD risk for VA women, particularly in young and racial/ethnic 
    minority women. See the reference: Jeon‐Slaughter, H., Chen, X., Tsai, S., Ramanan, B., & Ebrahimi, R. 
    (2021) <doi:10.1161/JAHA.120.019217>.
	"""
	
	cran = "vaRiskScore" 

	version("1.1.0", md5="0b9e366e7afe15740f6238ff5ba87cc0")

