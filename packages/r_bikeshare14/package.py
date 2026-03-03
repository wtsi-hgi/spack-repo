# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBikeshare14(RPackage):
	"""Bay Area Bike Share Trips in 2014

	Anonymised Bay Area bike share trip data for the year 2014. 
    Also contains additional metadata on stations and weather.
	"""
	
	homepage = "https://github.com/arunsrinivasan/bikeshare14"
	cran = "bikeshare14" 

	version("0.1.4", md5="5760aa033ec565bfa746226d02bfd450", url="https://cran.r-project.org/src/contrib/bikeshare14_0.1.4.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
