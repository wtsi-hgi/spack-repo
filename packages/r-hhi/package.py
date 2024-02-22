# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHhi(RPackage):
	"""Calculate and Visualize the Herfindahl-Hirschman Index

	Based on the aggregated shares retained by individual firms or actors within a market or space, the Herfindahl-Hirschman Index (HHI) measures the level of concentration in a space. This package allows for intuitive and straightforward computation of HHI scores, requiring placement of objects of interest directly into the function. The package also includes a plot function for quick visual display of an HHI time series using any measure of time (year, quarter, month, etc.). For usage, please cite the Journal of Open Source Software paper associated with the package: Waggoner, Philip D. (2018) <doi:10.21105/joss.00828>.
	"""
	
	cran = "hhi" 

	version("1.2.0", md5="b18681f22603aae88b0181b08138b88c")

	depends_on("r-ggplot2", type=("build", "run"))
