# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginCpd(RPackage):
	"""R Commander Plug-in for Complex Pearson Distributions

	Provides an 'Rcmdr' plug-in based on the 'cpd' package.
	"""
	
	cran = "RcmdrPlugin.cpd" 

	version("0.2.0", md5="8b81ff730c30a6eb67e89e76f039fbf9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cpd@0.3:", type=("build", "run"))
	depends_on("r-rcmdrmisc@2.7.2:", type=("build", "run"))
	depends_on("r-rcmdr@2.7.0:", type=("build", "run"))
