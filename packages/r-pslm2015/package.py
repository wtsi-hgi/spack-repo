# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPslm2015(RPackage):
	"""Pakistan Social and Living Standards Measurement Survey 2014-15

	Data and statistics of Pakistan Social and Living Standards Measurement (PSLM) survey 2014-15 from Pakistan Bureau of Statistics (<http://www.pbs.gov.pk/>).
	"""
	
	homepage = "https://github.com/MYaseen208/PSLM2015"
	cran = "PSLM2015" 

	version("0.2.0", md5="86f46adcf778f3ec24668cf151a9dae8", url="https://cran.r-project.org/src/contrib/PSLM2015_0.2.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
