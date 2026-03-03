# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlarmdata(RPackage):
	"""Download, Merge, and Process Redistricting Data

	
    Utility functions to download and process data produced by the ALARM Project,
    including 2020 redistricting files Kenny and McCartan (2021) 
    <https://alarm-redist.org/posts/2021-08-10-census-2020/> and the 50-State 
    Redistricting Simulations of McCartan, Kenny, Simko, Garcia, Wang, Wu, 
    Kuriwaki, and Imai (2022) <doi:10.7910/DVN/SLCD3E>. The package extends 
    the data introduced in McCartan, Kenny, Simko, Garcia, Wang, Wu, Kuriwaki,
    and Imai (2022) <doi:10.1038/s41597-022-01808-2> to also include states with 
    only a single district.
	"""
	
	homepage = "https://github.com/alarm-redist/alarmdata/"
	cran = "alarmdata" 

	version("0.2.1", md5="a5c064784d9e3c33d0948a897fb4d036")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dataverse", type=("build", "run"))
	depends_on("r-censable", type=("build", "run"))
	depends_on("r-geomander@2.1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-redist@4.2:", type=("build", "run"))
	depends_on("r-redistmetrics", type=("build", "run"))
	depends_on("r-tinytiger", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
