# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvirem(RPackage):
	"""Generation of ENVIREM Variables

	Generation of bioclimatic rasters that are complementary to the typical 19 bioclim variables.  
	"""
	
	homepage = "https://github.com/ptitle/envirem"
	cran = "envirem" 

	version("3.0", md5="ddceb7e25599bf82d82556e88134759e")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-palinsol", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
