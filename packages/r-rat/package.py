# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRat(RPackage):
	"""Research Assessment Tools

	Includes algorithms to assess research productivity and patterns, such as the h-index and i-index. Cardoso et al. (2022) Cardoso, P., Fukushima, C.S. & Mammola, S. (2022) Quantifying the internationalization and representativeness in research. Trends in Ecology and Evolution, 37: 725-728.
	"""
	
	cran = "RAT" 

	version("0.3.1", md5="cad55fe2fd82b05786c78b3b9190e49d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
