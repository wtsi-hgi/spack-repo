# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirectlabels(RPackage):
	"""Direct Labels for Multicolor Plots

	An extensible framework
 for automatically placing direct labels onto multicolor 'lattice' or
 'ggplot2' plots.
 Label positions are described using Positioning Methods
 which can be re-used across several different plots.
 There are heuristics for examining "trellis" and "ggplot" objects
 and inferring an appropriate Positioning Method.
	"""
	
	homepage = "https://github.com/tdhock/directlabels"
	cran = "directlabels" 

	version("2024.1.21", md5="7b77108461c30d70d2aff70222d5a730")

	depends_on("r-quadprog", type=("build", "run"))
