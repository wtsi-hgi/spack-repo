# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkmisc(RPackage):
	"""Miscellaneous Functions from M. Kohl

	Contains several functions for statistical data analysis; e.g. for sample size and power calculations, computation of confidence intervals and tests, and generation of similarity matrices.
	"""
	
	homepage = "https://github.com/stamats/MKmisc"
	cran = "MKmisc" 

	version("1.9", md5="b6db9fab8b0efac8c5f32509b8d1f026")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
