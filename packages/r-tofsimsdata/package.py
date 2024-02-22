# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTofsimsdata(RPackage):
	"""Import, process and analysis of ToF-SIMS imaging data

	This packages contains data to be used with the 'tofsims' package.
	"""
	
	bioc = "tofsimsData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/tofsimsData_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/tofsimsData/tofsimsData_1.30.0.tar.gz"]

	version("1.30.0", md5="57fe35de7b03ee4f3ca07540949a6b5e")

	depends_on("r@3.2:", type=("build", "run"))

	# experiment