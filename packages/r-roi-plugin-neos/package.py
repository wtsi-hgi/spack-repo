# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginNeos(RPackage):
	"""'NEOS' Plug-in for the 'R' Optimization Interface

	Enhances the 'R' Optimization Infrastructure ('ROI') package
             with a connection to the 'neos' server. 'ROI' optimization
             problems can be directly be sent to the 'neos' server
             and solution obtained in the typical 'ROI' style.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.neos" 

	version("1.0-2", md5="dd7c91284d1ae25973cf33e1e72a6045")

	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-xmlrpc2", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
