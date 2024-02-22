# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrabsvg(RPackage):
	"""Granularity-Based Spatially Variable Genes Identifications

	Identifying spatially variable genes is critical in linking molecular cell functions with tissue phenotypes. This package implemented a granularity-based dimension-agnostic tool for the identification of spatially variable genes. The detailed description of this method is available at Wang, J. and Li, J. et al. 2023 (Wang, J. and Li, J. (2023), <doi:10.1038/s41467-023-43256-5>).
	"""
	
	cran = "GrabSVG" 

	version("0.0.2", md5="3dd20bcb216350551ff4266594b4807b")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
