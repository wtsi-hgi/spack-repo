# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmission(RPackage):
	"""Hospital Readmission Data for Patients with Diabetes

	Clinical care data from 130 U.S. hospitals in the years 1999-2008
    adapted from the study Strack et al. (2014) <doi:10.1155/2014/781670>. 
    Each row describes an "encounter" with a patient with diabetes, including 
    variables on demographics, medications, patient history, diagnostics, 
    payment, and readmission.
	"""
	
	cran = "readmission" 

	version("0.1.0", md5="dc0ef5ef09929aaa2a4f45df205e1de5")

	depends_on("r@2.10:", type=("build", "run"))
