# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimbindprofiles(RPackage):
	"""Similar Binding Profiles

	SimBindProfiles identifies common and unique binding regions in genome tiling array data. This package does not rely on peak calling, but directly compares binding profiles processed on the same array platform. It implements a simple threshold approach, thus allowing retrieval of commonly and differentially bound regions between datasets as well as events of compensation and increased binding.
	"""
	
	bioc = "SimBindProfiles" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SimBindProfiles_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SimBindProfiles/SimBindProfiles_1.40.0.tar.gz"]

	version("1.40.0", md5="9785a8acda5c3423edaefd09f14e6ca2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ringo", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
