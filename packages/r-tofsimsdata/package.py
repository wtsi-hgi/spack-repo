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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/tofsimsData_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/tofsimsData/tofsimsData_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="8dfe97fc644d125882393ad9722a9569d88435d457ead0e11daf06b6f214d6a1")

	depends_on("r@3.2:", type=("build", "run"))

