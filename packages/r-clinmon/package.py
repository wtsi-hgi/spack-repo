# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinmon(RPackage):
	"""Hemodynamic Calculations from Clinical Monitoring

	
   Every research team have their own script for calculation of hemodynamic indexes. 
   This package makes it possible  to insert a long-format dataframe, and add both 
   periods of interest (trigger-periods), and delete artifacts with deleter-files.
	"""
	
	homepage = "https://github.com/lilleoel/clinmon"
	cran = "clinmon" 

	version("0.6.0", md5="c9bf7bf1430f9ad0b2ac0fdcf0100553")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-signal@0.7.6:", type=("build", "run"))
