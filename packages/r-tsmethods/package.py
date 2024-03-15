# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsmethods(RPackage):
	"""Time Series Methods

	Generic methods for use in a time series probabilistic framework, allowing for a common calling convention across packages. Additional methods for time series prediction ensembles and probabilistic plotting of predictions is included. A more detailed description is available at <https://www.nopredict.com/packages/tsmethods> which shows the currently implemented methods in the 'tsmodels' framework. 
	"""
	
	homepage = "https://www.nopredict.com/packages/tsmethods"
	cran = "tsmethods" 

	version("1.0.0", md5="938e44c5ef1684d26fc03fa161a9dfb9")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
