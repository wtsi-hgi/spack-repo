# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrocal(RPackage):
	"""Hydraulic Roughness Calculator

	Estimates frictional constants for hydraulic analysis 
    of rivers. This HYDRaulic ROughness CALculator (HYDROCAL) was previously 
    developed as a spreadsheet tool and accompanying documentation by McKay and
    Fischenich (2011, <https://erdc-library.erdc.dren.mil/jspui/bitstream/11681/2034/1/CHETN-VII-11.pdf>).
	"""
	
	homepage = "GitHub"
	cran = "HYDROCAL" 

	version("1.0.0", md5="bbf6a0b7b002c59f9e730e182c53fdb0")

	depends_on("r@4.1:", type=("build", "run"))
