# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpeakchrom(RPackage):
	"""Tools for Chromatographic Column Characterization and Modelling
Chromatographic Peak

	The quantitative measurement and detection of molecules in HPLC should be carried out by an accurate description of chromatographic peaks. In this package non-linear fitting using a modified Gaussian model with a parabolic variance (PVMG) has been implemented to obtain the retention time and height at the peak maximum. This package also includes the traditional Van Deemter approach and two alternatives approaches to characterize chromatographic column.
	"""
	
	cran = "RpeakChrom" 

	version("1.1.0", md5="898651c59793f4f6a09f123cc6cb4ae1")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ptw", type=("build", "run"))
