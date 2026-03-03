# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDurga(RPackage):
	"""Effect Size Estimation and Visualisation

	An easy-to-use yet powerful system for plotting grouped data effect sizes.
    Various types of effect size can be estimated, then plotted together with a
    representation of the original data. Select from many possible data representations
    (box plots, violin plots, raw data points etc.), and combine as desired.
    'Durga' plots are implemented in base R, so are compatible with base R methods
    for combining plots, such as 'layout()'. See Khan & McLean (2023) 
    <doi:10.1101/2023.02.06.526960>.
	"""
	
	homepage = "https://github.com/KhanKawsar/EstimationPlot"
	cran = "Durga" 

	version("2.0", md5="8368539e3939d1aa8e23c259bd369d05")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vipor", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
