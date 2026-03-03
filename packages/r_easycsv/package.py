# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasycsv(RPackage):
	"""Load Multiple 'csv' and 'txt' Tables

	Allows users to easily read multiple comma separated tables and create a data frame under the same name.
    Is able to read multiple comma separated tables from a local directory, a zip file or a zip file on a remote directory. 
	"""
	
	homepage = "https://github.com/bogind/easycsv"
	cran = "easycsv" 

	version("1.0.8", md5="8f0af88db5c05b948f585bd954fa26e6")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
