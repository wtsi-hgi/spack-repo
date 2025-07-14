# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffycompdata(RPackage):
	"""affycomp data

	Data needed by the affycomp package.
	"""
	
	homepage = "https://bioconductor.org/packages/affycompData"
	bioc = "affycompData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/affycompData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/affycompData/affycompData_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="04ef8a0119f30b70cde5434cb5144823065e6db355a7cc3369c91d49d87a7ca0")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.3.3:", type=("build", "run"))
	depends_on("r-affycomp", type=("build", "run"))

