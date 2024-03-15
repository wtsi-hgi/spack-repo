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

	version("0.40.0", md5="d6fb25eaad39c714024ed855c8c9c87d")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

	# experiment