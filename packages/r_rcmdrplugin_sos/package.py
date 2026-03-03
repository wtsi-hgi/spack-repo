# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginSos(RPackage):
	"""Efficiently search the R help pages

	Rcmdr interface to the 'sos' package. The plug-in renders
  the 'sos' searching functionality easily accessible via the Rcmdr
  menus. It also simplifies the task of performing multiple searches and 
  subsequently obtaining the union or the intersection of the results. 
	"""
	
	cran = "RcmdrPlugin.sos" 

	version("0.3-0", md5="bd4146ea91eef510d2f2d8700d178bd8")

	depends_on("r-sos@1.2.3:", type=("build", "run"))
	depends_on("r-rcmdr@2.0.1:", type=("build", "run"))
	depends_on("r-tcltk2@1.2.7:", type=("build", "run"))
