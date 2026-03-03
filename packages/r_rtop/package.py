# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtop(RPackage):
	"""Interpolation of Data with Variable Spatial Support

	Data with irregular spatial support, such as runoff related data or data from administrative units, can with 'rtop' be interpolated to locations without observations with the top-kriging method. A description of the package is given by Skøien et al (2014) <doi:10.1016/j.cageo.2014.02.009>.
	"""
	
	cran = "rtop" 

	version("0.6-9", md5="0e3ee52c3e7aa16c5ca31315d7afc99c")

	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
