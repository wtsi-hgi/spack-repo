# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorphoscape(RPackage):
	"""Computation and Visualization of Adaptive Landscapes

	Implements adaptive landscape methods first described by Polly et al. (2016) <doi:10.1080/02724634.2016.1111225> for the integration, analysis and visualization of biological trait data on a phenotypic morphospace - typically defined by shape metrics.
	"""
	
	homepage = "https://blakedickson.github.io/Morphoscape/"
	cran = "Morphoscape" 

	version("1.0.2", md5="8ba3bdc683a7b4550259cef55ad0c1cf")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-spatial", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-alphahull", type=("build", "run"))
