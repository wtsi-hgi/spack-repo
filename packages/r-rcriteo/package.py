# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcriteo(RPackage):
	"""Loading Criteo Data into R

	Aims at loading Criteo online advertising campaign data into R.
    Criteo <http://www.criteo.com/> is an online advertising service that enables
    advertisers to display commercial ads to web users. The package provides
    an authentication process for R with the Criteo API <http://kb.criteo.com/
    advertising/content/5/27/en/api.html>. Moreover, the package features an
    interface to query campaign data from the Criteo API. The data can be downloaded
    and will be transformed into a R data frame.
	"""
	
	homepage = "http://jburkhardt.github.io/RCriteo/"
	cran = "RCriteo" 

	version("1.0.2", md5="4dff12a886f11851dd73018a0ea98f38")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
