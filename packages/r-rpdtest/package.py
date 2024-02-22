# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpdtest(RPackage):
	"""A New Type of Test Statistic and Method for Multinomial
Goodness-of-Fit Test

	Performs multinomial goodness-of-fit test on multinomially distributed data using the Randomized phi-divergence test statistics. Details of this kind of statistics can be found at Nikita Puchkin, Vladimir Ulyanov (2023) <doi:10.1214/22-AIHP1299>.
	"""
	
	cran = "RPDTest" 

	version("0.0.1", md5="9fd0d7fdc0935a3b291a7cbe6a7d17b9")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
