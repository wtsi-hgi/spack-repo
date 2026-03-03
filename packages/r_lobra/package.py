# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLobra(RPackage):
	"""Generalized Spline Mixed Effect Models for Longitudinal Breath
Data

	Automated analysis and modeling of longitudinal 'omics' data (e.g. breath 'metabolomics') using generalized spline mixed effect models. Including automated filtering of noise parameters and determination of breakpoints.
	"""
	
	cran = "LoBrA" 

	version("1.0", md5="5a0bee01d01083aed31325da0c84151f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lawstat", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
