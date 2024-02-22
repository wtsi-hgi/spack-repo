# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLightningr(RPackage):
	"""Tools for Communication with Lightning-Viz Server

	The purpose of this package is to enable usage of lightningviz server to be accessible from R. The
   server itself can be found at http://lightning-viz.org/ and is required to work with this package. Package
   by itself cannot and will not create any visualizations.
	"""
	
	homepage = "https://github.com/Ermlab/lightining-rstat/"
	cran = "LightningR" 

	version("1.0.2", md5="46c3052067b7335d7c430d7ab832b323")

	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
