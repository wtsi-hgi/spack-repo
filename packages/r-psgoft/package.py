# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsgoft(RPackage):
	"""Modified Lilliefors Goodness-of-Fit Normality Test

	Presentation of a new goodness-of-fit normality test based on the Lilliefors method. For details on this method see: Sulewski (2019) <doi:10.1080/03610918.2019.1664580>.
	"""
	
	cran = "PSGoft" 

	version("0.0.1", md5="68dd34280871b3c63ed8867c06f0c349")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
