# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCentralplot(RPackage):
	"""Show the Strength of Relationships Between Centre and Peripheral
Items

	The degree of correlation between centre and peripheral items are shown by the length of the line between them. You can self-define the length by inputing the "distance" parameter. For example, you can input (1 - Pearson's correlation coefficient) as "distance" so that the stronger the correlation between centre and peripheral item, the nearer they will be in this plot. Also, If you do a hypothesis test and the null hypothesis is centre and peripheral items are the same, you can input -log(P) as distance. To sum up, the stronger the correlation between centre and peripheral is, the smaller the "distance" parameter should be. Due to its high degree of freedom, it can be applied to many different circumstance.
	"""
	
	cran = "centralplot" 

	version("0.1.0", md5="753893ff21782ca09ddb75348673657a")

	depends_on("r-ggplot2", type=("build", "run"))
