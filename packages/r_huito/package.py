# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuito(RPackage):
	"""Reproducible and Flexible Label Design

	An open-source R package to deploys reproducible and flexible labels using layers. 
  The 'huito' package is part of the 'inkaverse' project for developing different procedures and
  tools used in plant science and experimental designs. 
  Learn more about the 'inkaverse' project at <https://inkaverse.com/>.
	"""
	
	homepage = "https://huito.inkaverse.com/"
	cran = "huito" 

	version("0.2.4", md5="65f30d495d6f1259aa94b2441d27d9f6")

	depends_on("r-magick", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-qrcode", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
