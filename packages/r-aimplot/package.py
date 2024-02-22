# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAimplot(RPackage):
	"""Create Pie Like Plot for Completeness

	Create a pie like plot to visualise if the aim or several aims of a
             project is achieved or close to be achieved i.e the aim is achieved when the point is at the
             center of the pie plot. Imagine it's like a dartboard and the center means 100%
             completeness/achievement. Achievement can also be understood as 100%
             coverage. The standard distribution of completeness allocated in the pie plot
             is 50%, 80% and 100% completeness.
	"""
	
	cran = "aimPlot" 

	version("1.0.0", md5="fac9f46e71108cb2670070202976496f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
