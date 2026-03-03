# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnxietysleep(RPackage):
	"""Sleep Quality and Anxiety in Confinement

	Data from the anxiety and confinement study from Alvarado-Aravena et al. (2022) <doi:10.3390/bs12100398>.
	"""
	
	homepage = "https://github.com/NIM-ACh/AnxietySleep"
	cran = "AnxietySleep" 

	version("0.0.1", md5="87fee83bceda2e6f659cf87ae38d7866")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
