# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrimedata(RPackage):
	"""Access Crime Data from the Open Crime Database

	Gives convenient access to publicly available police-recorded open
    crime data from large cities in the United States that are included in the
    Crime Open Database <https://osf.io/zyaqn/>.
	"""
	
	homepage = "http://pkgs.lesscrime.info/crimedata/"
	cran = "crimedata" 

	version("0.3.5", md5="b828df73e0c3822ac7bacc43a8341f94")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-osfr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
