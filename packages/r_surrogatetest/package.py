# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrogatetest(RPackage):
	"""Early Testing for a Treatment Effect using Surrogate Marker
Information

	Provides functions to test for a treatment effect in terms of the difference in survival between a treatment group and a control group using surrogate marker information obtained at some early time point in a time-to-event outcome setting. Nonparametric kernel estimation is used to estimate the test statistic and perturbation resampling is used for variance estimation. More details will be available in the future in: Parast L, Cai T, Tian L (2019) ``Using a Surrogate Marker for Early Testing of a Treatment Effect" Biometrics, 75(4):1253-1263. <doi:10.1111/biom.13067>.
	"""
	
	cran = "SurrogateTest" 

	version("1.3", md5="1b6c1a1b0582305d0c291814d0016c61")

	depends_on("r-survival", type=("build", "run"))
