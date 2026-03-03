# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCd(RPackage):
	"""CD Data for Entity Resolution

	Duplicated music data (pre-processed and formatted) for entity resolution. The total size of the data set is 9763. There are respective gold standard records that are labeled and can be considered as a unique identifier.  
	"""
	
	homepage = "https://github.com/resteorts/cd"
	cran = "cd" 

	version("0.1.0", md5="e3d55d6367c5520ba5b8fc4abbef4e7d")

	depends_on("r@3.4:", type=("build", "run"))
