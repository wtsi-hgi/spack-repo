# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPisart(RPackage):
	"""Small Example Response and Response Time Data from PISA 2018

	Scored responses and responses times from the Canadian subsample of the PISA 2018 assessment, accessible as the "Cognitive items total time/visits data file" by OECD (2020) <https://www.oecd.org/pisa/data/2018database/>. 
	"""
	
	cran = "pisaRT" 

	version("2.0.2", md5="ed688cbafe185ea7f7c4968aa6e5b2ae")

	depends_on("r@2.10:", type=("build", "run"))
