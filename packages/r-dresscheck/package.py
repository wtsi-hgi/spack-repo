# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDresscheck(RPackage):
	"""data and software for checking Dressman JCO 25(5) 2007

	data and software for checking Dressman JCO 25(5) 2007
	"""
	
	bioc = "dressCheck" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/dressCheck_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/dressCheck/dressCheck_0.40.0.tar.gz"]

	version("0.40.0", sha256="e3a7d8e5611aff83fb416d003e8a8c32e2d7d4661f7ec69b3c2b07e37c6566d5")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

