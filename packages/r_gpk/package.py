# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpk(RPackage):
	"""100 Data Sets for Statistics Education

	Collection of datasets as prepared by Profs. A.P. Gore, S.A. Paranjape, and M.B. Kulkarni of Department of Statistics, Poona University, India. With their permission, first letter of their names forms the name of this package, the package has been built by me and made available for the benefit of R users. This collection requires a rich class of models and can be a very useful building block for a beginner. 
	"""
	
	cran = "gpk" 

	version("1.0", md5="6d3a50975536dd3b5a6094f942790b51")

