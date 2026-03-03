# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsos(RPackage):
	"""Data Sets and Functions Used in Multivariate Statistics: Old
School by John Marden

	Multivariate Analysis methods and data sets used
    in John Marden's book Multivariate Statistics: Old School (2015) <ISBN:978-1456538835>.
    This also serves as a companion package for the 
    STAT 571: Multivariate Analysis course offered by the Department of Statistics
    at the University of Illinois at Urbana-Champaign ('UIUC'). 
	"""
	
	homepage = "https://github.com/coatless/msos"
	cran = "msos" 

	version("1.2.0", md5="3c32d39f8d0e570d294fa1cbfa57ee25")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
