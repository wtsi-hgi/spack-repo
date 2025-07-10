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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RMassBankData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RMassBankData/RMassBankData_1.40.0.tar.gz"]

	version("1.40.0", sha256="d80d62e6a6353d1854aff8ce84efb59baf297cd7ca6ab2d6d8210620102618a4")


