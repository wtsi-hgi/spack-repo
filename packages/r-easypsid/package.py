# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasypsid(RPackage):
	"""Reading, Formatting, and Organizing the Panel Study of Income
Dynamics (PSID)

	Provides various functions for reading and preparing the Panel Study of Income Dynamics (PSID) for longitudinal analysis, including functions that read the PSID's fixed width format files directly into R, rename all of the PSID's longitudinal variables so that recurring variables have consistent names across years, simplify assembling longitudinal datasets from cross sections of the PSID Family Files, and export the resulting PSID files into file formats common among other statistical programming languages ('SAS', 'STATA', and 'SPSS').
	"""
	
	cran = "easyPSID" 

	version("0.1.2", md5="a65e1bb1565076ba6792047c5731adc1")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-laf@0.6:", type=("build", "run"))
	depends_on("r-foreign@0.8.67:", type=("build", "run"))
