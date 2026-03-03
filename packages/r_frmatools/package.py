# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrmatools(RPackage):
	"""Frozen RMA Tools

	Tools for advanced use of the frma package.
	"""
	
	homepage = "http://bioconductor.org"
	bioc = "frmaTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/frmaTools_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/frmaTools/frmaTools_1.54.0.tar.gz"]

	version("1.54.0", md5="270e71dc903bb77add1154782cf17342")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
