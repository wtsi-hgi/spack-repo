# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImbalancedatrel(RPackage):
	"""Relocated Data Oversampling for Imbalanced Data Classification

	Relocates oversampled data from a specific oversampling method to
    cover area determined by pure and proper class cover catch digraphs (PCCCD). 
    It prevents any data to be generated in class overlapping area. 
	"""
	
	cran = "imbalanceDatRel" 

	version("0.1.5", md5="cfe3df1c28584d392685db54c923a6cd")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcccd", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-smotewb", type=("build", "run"))
