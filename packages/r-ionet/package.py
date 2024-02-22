# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIonet(RPackage):
	"""Network Analysis for Input-Output Tables

	Network functionalities specialized for data generated from input-output tables.
	"""
	
	homepage = "https://github.com/Carol-seven/ionet"
	cran = "ionet" 

	version("0.2.2", md5="8522949036ee30a21a6b0ec4a696d909")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
