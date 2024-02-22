# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMand(RPackage):
	"""Multivariate Analysis for Neuroimaging Data

	Several functions can be used to analyze neuroimaging data using multivariate methods based on the 'msma' package. The functions used in the book entitled "Multivariate Analysis for Neuroimaging Data" (2021, ISBN-13: 978-0367255329) are contained.
	"""
	
	cran = "mand" 

	version("2.0", md5="81534ac134b00046ea46ba71c5b1a489")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msma", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-oro-dicom", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
