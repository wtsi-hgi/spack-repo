# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRriskdistributions(RPackage):
	"""Fitting Distributions to Given Data or Known Quantiles

	Collection of functions for fitting distributions to given data or
    by known quantiles. Two main functions fit.perc() and fit.cont() provide
    users a GUI that allows to choose a most appropriate distribution without
    any knowledge of the R syntax. Note, this package is a part of the 'rrisk'
    project.
	"""
	
	homepage = "http://www.bfr.bund.de/cd/52158"
	cran = "rriskDistributions" 

	version("2.1.2", md5="4e9f7eaa0702ee73c06d84c0bf4dfddf")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("tcl", type=("build", "link", "run"))
	depends_on("tk", type=("build", "link", "run"))
	depends_on("tktable", type=("build", "link", "run"))
