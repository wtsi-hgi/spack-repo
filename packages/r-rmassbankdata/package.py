# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmassbankdata(RPackage):
	"""Test dataset for RMassBank

	Example spectra, example compound list(s) and an example annotation list for a narcotics dataset; required to test RMassBank. The package is described in the man page for RMassBankData. Includes new XCMS test data.
	"""
	
	bioc = "RMassBankData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/RMassBankData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/RMassBankData/RMassBankData_1.40.0.tar.gz"]

	version("1.40.0", md5="ac6f883e962890eebb03c2368be8bcdc")


	# experiment