# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpc2017(RPackage):
	"""Pakistan Population Census 2017

	Provides data sets and functions for exploration of Pakistan Population Census 2017 (<http://www.pbscensus.gov.pk/>).
	"""
	
	homepage = "https://github.com/MYaseen208/PakPC2017"
	cran = "PakPC2017" 

	version("1.0.0", md5="1b0436bcc8ea92f1bc0f6f90dc25470f", url="https://cran.r-project.org/src/contrib/PakPC2017_1.0.0.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
