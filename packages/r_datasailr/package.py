# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasailr(RPackage):
	"""Row by Row Data Processing Tool, Using 'DataSailr' Script

	A row by row data processing tool. You can write data processing code in 'DataSailr' script which is specially intended for data manipulation. The package uses 'libsailr' (C/C++ library) for its 'DataSailr' code parsing and its execution.
	"""
	
	homepage = "https://datasailr.io"
	cran = "datasailr" 

	version("0.8.11", md5="2632f02ed0c4034cea5198b4085f0d08")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
