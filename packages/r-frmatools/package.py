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

    version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="fddae3f2e3f52d31ababe1e76d6ed3530e0329f91300a6c256f683df9623917f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
