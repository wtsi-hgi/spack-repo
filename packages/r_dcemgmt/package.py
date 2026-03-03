# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcemgmt(RPackage):
	"""DCE Data Reshaping and Processing

	Prepare the results of a DCE to be analysed through choice models.'DCEmgmt' reshapes DCE data from wide to long format considering the special characteristics of a DCE. 'DCEmgmt' includes the function 'DCEestm' which estimates choice models once the database has been reshaped with 'DCEmgmt'.
	"""
	
	cran = "DCEmgmt" 

	version("0.0.1", md5="c458fe6a70e5326d49e3966724718a8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mlogit@1.0.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
