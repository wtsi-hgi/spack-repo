# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlineretail(RPackage):
	"""Online Retail Dataset

	Transactions occurring for a UK-based and registered, non-store online 
    retail between 01/12/2010 and 09/12/2011 (Chen et. al., 2012, <doi:10.1145/1835804.1835882>). 
    This dataset is included in this package with the donor's permission, Dr. Daqing Chen.
	"""
	
	homepage = "https://github.com/allanvc/onlineretail/"
	cran = "onlineretail" 

	version("0.1.2", md5="c5b91d2683e83aadd8c2b0652bbb4d39")

	depends_on("r@3.5:", type=("build", "run"))
