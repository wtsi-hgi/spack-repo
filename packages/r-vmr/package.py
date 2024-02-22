# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVmr(RPackage):
	"""Virtual Machines for R

	Manage, provision and use Virtual Machines pre-configured for R.
             Develop, test and build package in a clean environment.
             'Vagrant' tool and a provider (such as 'Virtualbox') have to be installed.
	"""
	
	homepage = "https://gitlab.com/rstuff/vmr"
	cran = "vmr" 

	version("0.0.6", md5="3550e007b45364dc17ee0d061abf0319")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
