# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpstudy(RPackage):
	"""Tools for Actuarial Experience Studies

	Experiences studies are an integral component of the actuarial 
    control cycle. Regardless of the decrement or policyholder behavior of 
    interest, the analyses conducted is often the same. Ultimately, this 
    package aims to reduce time spent writing the same code used for 
    different experience studies, therefore increasing the time for to uncover
    new insights inherit within the relevant experience.
	"""
	
	homepage = "https://github.com/cb12991/expstudy"
	cran = "expstudy" 

	version("2.0.0", md5="5f985f2424a621a3a51e59c149273ad7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
