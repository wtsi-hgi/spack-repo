# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInqc(RPackage):
	"""Quality Control of Climatological Daily Time Series

	Collection of functions for quality control (QC) of climatological daily time series (e.g. the ECA&D station data).
	"""
	
	homepage = "https://github.com/INDECIS-Project/INQC"
	cran = "INQC" 

	version("2.0.5", md5="b6afee468ab9d7d8bc93f58feab6385a")

	depends_on("r-evd", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
