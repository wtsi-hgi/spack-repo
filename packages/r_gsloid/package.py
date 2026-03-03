# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsloid(RPackage):
	"""Global Sea Level and Oxygen Isotope Data

	Contains published data sets for global benthic d18O data for 
    0-5.3 Myr <doi:10.1029/2004PA001071> and global sea levels based 
    on marine sediment core data for 0-800 ka <doi:10.5194/cp-12-1-2016>.
	"""
	
	homepage = "https://github.com/benmarwick/gsloid"
	cran = "gsloid" 

	version("0.2.0", md5="3b30abb51fb363b8598071705a587ed3")

	depends_on("r@3.3:", type=("build", "run"))
