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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rawrr_1.10.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rawrr/rawrr_1.10.2.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.2", sha256="105fc356152755d3d6ff893a25c198e7b1b94a4ee632281f47a1507df1e8cff3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("mono", type=("build", "link", "run"))
