# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasetempseed(RPackage):
	"""Estimation of Seed Germination Base Temperature in Thermal
Modelling

	All the seeds do not germinate at a single point in time due to physiological mechanisms determined by temperature which vary among individual seeds in the population. Seeds germinate by following accumulation of thermal time in degree days/hours, quantified by multiplying the time of germination with excess of base temperature required by each seed for its germination, which follows log-normal distribution. The theoretical germination course can be obtained by regressing the rate of germination at various fractions against temperature (Garcia et al., 1982), where the fraction-wise regression lines intersect the temperature axis at base temperature and the methodology of determining optimum base temperature has been described by Ellis et al. (1987). This package helps to find the base temperature of seed germination using algorithms of Garcia et al. (1982) and Ellis et al. (1982) <doi:10.1093/JXB/38.6.1033> <doi:10.1093/jxb/33.2.288>.
	"""
	
	cran = "BaseTempSeed" 

	version("0.1.0", md5="5ee3e25216fe404fa204e85a6a2939a4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlcoptim", type=("build", "run"))
