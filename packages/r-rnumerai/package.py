# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnumerai(RPackage):
	"""Interface to the Numerai Machine Learning Tournament API

	Routines to interact with the Numerai Machine Learning Tournament
  API <https://numer.ai>. The functionality includes the ability to automatically download the
  current tournament data, submit predictions, and to get information for your
  user. 
	"""
	
	homepage = "https://github.com/Omni-Analytics-Group/Rnumerai"
	cran = "Rnumerai" 

	version("3.0.1", md5="9334618f338d1243169b27e514426387")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ghql", type=("build", "run"))
