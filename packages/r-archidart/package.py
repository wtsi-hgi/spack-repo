# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchidart(RPackage):
	"""Plant Root System Architecture Analysis Using DART and RSML
Files

	Analysis of complex plant root system architectures (RSA) using the output files created by Data Analysis of Root Tracings (DART), an open-access software dedicated to the study of plant root architecture and development across time series (Le Bot et al (2010) "DART: a software to analyse root system architecture and development from captured images", Plant and Soil, <DOI:10.1007/s11104-009-0005-2>), and RSA data encoded with the Root System Markup Language (RSML) (Lobet et al (2015) "Root System Markup Language: toward a unified root architecture description language", Plant Physiology, <DOI:10.1104/pp.114.253625>). More information can be found in Delory et al (2016) "archiDART: an R package for the automated computation of plant root architectural traits", Plant and Soil, <DOI:10.1007/s11104-015-2673-4>.
	"""
	
	homepage = "https://archidart.github.io/"
	cran = "archiDART" 

	version("3.4", md5="0d0b606dda0578c58e9de770fd2d261e")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
