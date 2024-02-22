# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventdatar(RPackage):
	"""Event Data Repository

	Event dataset repository including both real-life and artificial event logs. They can be used in combination with functionalities provided by the 'bupaR' packages. Janssenswillen et al. (2020) <http://ceur-ws.org/Vol-2703/paperTD7.pdf>.
	"""
	
	homepage = "https://bupar.net/"
	cran = "eventdataR" 

	version("0.3.1", md5="761635278112cc46b123edfca4da7aff")

	depends_on("r@3:", type=("build", "run"))
