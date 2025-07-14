# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRawrr(RPackage):
	"""Direct Access to Orbitrap Data and Beyond

	This package wraps the functionality of the RawFileReader .NET assembly. Within the R environment, spectra and chromatograms are represented by S3 objects. The package provides basic functions to download and install the required third-party libraries. The package is developed, tested, and used at the Functional Genomics Center Zurich, Switzerland.
	"""
	
	homepage = "https://github.com/fgcz/rawrr/"
	bioc = "rawrr"

	version("1.16.0", commit="9604eccdc30ae3123e3c39a45fbc29a0dd633732")
	version("1.10.2", commit="25ae3ee4cae629b7a5538f2999726b5532014eda")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("mono", type=("build", "link", "run"))
