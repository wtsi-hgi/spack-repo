# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrinvars(RPackage):
	"""Principal Variables

	Provides methods for reducing the number of features within a data set. See Bauer JO (2021) <doi:10.1145/3475827.3475832> and Bauer JO, Drabant B (2021) <doi:10.1016/j.jmva.2021.104754> for more information on principal loading analysis.
	"""
	
	homepage = "https://github.com/Ronho/prinvars"
	cran = "prinvars" 

	version("1.0.0", md5="1af4af7ea70c0d9c2e81490b4b629c7e")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
