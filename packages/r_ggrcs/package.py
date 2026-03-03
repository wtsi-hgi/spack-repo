# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrcs(RPackage):
	"""Draw Histograms and Restricted Cubic Splines (RCS)

	You can use this function to easily draw a combined histogram and restricted cubic spline. 
    The function draws the graph through 'ggplot2'. RCS fitting requires the use of the rcs() function of the 'rms' package. 
    Can fit cox regression, logistic regression. This method was described by Per Kragh (2003) <doi:10.1002/sim.1497>.
	"""
	
	cran = "ggrcs" 

	version("0.3.8", md5="afac9452c00647624516cc7880bd72af")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
