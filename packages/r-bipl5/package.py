# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBipl5(RPackage):
	"""Construct Reactive Calibrated Axes Biplots

	A modern view on the principal component analysis biplot with 
    calibrated axes. Create principal component analysis biplots rendered in 
    HTML with significant reactivity embedded within the plot. Furthermore, 
    the traditional biplot view is enhanced by translated axes with inter-class
    kernel densities superimposed. For more information on biplots, see 
    Gower, J.C., Lubbe, S. and le Roux, N.J. (2011, ISBN: 978-0-470-01255-0).
	"""
	
	cran = "bipl5" 

	version("1.0.2", md5="c28e0a94af15d73fa8da29b9daf281dc", url="https://cran.r-project.org/src/contrib/bipl5_1.0.2.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-crayon@1.5.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.6.2:", type=("build", "run"))
	depends_on("r-knitr@1.43:", type=("build", "run"))
	depends_on("r-plotly@4.10.2:", type=("build", "run"))
