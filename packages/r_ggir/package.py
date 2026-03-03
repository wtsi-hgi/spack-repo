# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgir(RPackage):
	"""Raw Accelerometer Data Analysis

	A tool to process and analyse data collected with wearable raw acceleration sensors as described in Migueles and colleagues (JMPB 2019), and van Hees and colleagues (JApplPhysiol 2014; PLoSONE 2015). The package has been developed and tested for binary data from 'GENEActiv' <https://activinsights.com/>, binary (.gt3x) and .csv-export data from  'Actigraph' <https://theactigraph.com> devices, and binary (.cwa) and .csv-export data from 'Axivity' <https://axivity.com>. These devices are currently widely used in research on human daily physical activity. Further, the package can handle accelerometer data file from any other sensor brand providing that the data is stored in csv format. Also the package allows for external function embedding.
	"""
	
	homepage = "https://github.com/wadpac/GGIR/"
	cran = "GGIR" 

	version("3.0-9", md5="b3ab08ba1baac62b72b02ff74bf1d099")
	version("3.0-6", md5="03023fad881692aa3a25b43bf1413815")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-unisensr", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggirread", type=("build", "run"))
	depends_on("r-actcr", type=("build", "run"))
	depends_on("r-read-gt3x", type=("build", "run"))
