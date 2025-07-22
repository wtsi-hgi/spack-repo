# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodelink(RPackage):
	"""Manipulation of Codelink microarray data

	This package facilitates reading, preprocessing and manipulating Codelink microarray data. The raw data must be exported as text file using the Codelink software.
	"""
	
	homepage = "https://github.com/ddiez/codelink"
	bioc = "codelink" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/codelink_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/codelink/codelink_1.70.0.tar.gz"]

	version("1.76.0", tag="RELEASE_3_21")
	version("1.70.0", sha256="95d29d16bb91b5cdabfff66f03d4dec3728a73aa65b72b3fc16f5bf0e2d3b790")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
