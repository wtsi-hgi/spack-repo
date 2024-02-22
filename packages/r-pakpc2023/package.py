# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpc2023(RPackage):
	"""Pakistan Population Census 2023

	Provides data sets and functions for exploration of Pakistan Population Census 2023 (<https://www.pbs.gov.pk/>).
	"""
	
	homepage = "https://github.com/myaseen208/PakPC2023"
	cran = "PakPC2023" 

	version("0.1.0", md5="3ed101b2b469b23e57ec24080c00d444", url="https://cran.r-project.org/src/contrib/PakPC2023_0.1.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
