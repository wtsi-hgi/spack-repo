# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcoletum(RPackage):
	"""Access your Coletum's Data from API

	Get your data (forms, structures, answers) from Coletum 
    <https://coletum.com> to handle and analyse.
	"""
	
	homepage = "https://github.com/geo-sapiens/RColetum"
	cran = "RColetum" 

	version("0.2.2", md5="9e42b9ff29002ce60c992021e74ef806")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
