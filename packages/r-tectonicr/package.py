# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTectonicr(RPackage):
	"""Analyzing the Orientation of Maximum Horizontal Stress

	Models the direction of the maximum horizontal stress using
    relative plate motion parameters. Statistical algorithms to evaluate
    the modeling results compared with the observed data. Provides plots
    to visualize the results. Methods described in Stephan et al. (2023)
    <doi:10.1038/s41598-023-42433-2> and Wdowinski (1998)
    <doi:10.1016/S0079-1946(98)00091-3>.
	"""
	
	homepage = "https://tobiste.github.io/tectonicr/"
	cran = "tectonicr" 

	version("0.2.95", md5="d7c6f3eac3b30f5d02443d80b484db50")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-smoothr", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
