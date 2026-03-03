# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKidneyEpi(RPackage):
	"""Kidney Functions: Clinical and Epidemiological

	Contains kidney care oriented functions.
			 Current version contains functions for calculation of:
			 - Kidney Donor Risk Index and Kidney Donor Profile Index for kidney transplant donors by Rao et al. (2009) <doi:10.1097/TP.0b013e3181ac620b>.
			 - Estimated glomerular filtration rate by CKD-EPI, MDRD and other equations.
			 Citation: Bikbov B. R open source programming code for calculation of the Kidney Donor Profile Index and Kidney Donor Risk Index. Kidney Diseases (2018) 4:269–272 <doi:10.1159/000492427> (the only citation for the whole package).
	"""
	
	homepage = "http://kidneyepidemiology.org/r/"
	cran = "kidney.epi" 

	version("1.2.0", md5="4ccef8d96926a32fe2010a4ff823da05")

	depends_on("r@3.4:", type=("build", "run"))
