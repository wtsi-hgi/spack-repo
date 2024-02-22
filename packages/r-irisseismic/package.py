# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrisseismic(RPackage):
	"""Classes and Methods for Seismic Data Analysis

	Provides classes and methods for seismic data analysis. The
             base classes and methods are inspired by the python code found in
             the 'ObsPy' python toolbox <https://github.com/obspy/obspy>. Additional classes and 
             methods support data returned by web services provided by the 'IRIS DMC'
             <http://service.iris.edu/>.
	"""
	
	cran = "IRISSeismic" 

	version("1.6.6", md5="d0535f70e52215ecb70ff09e7ae0093e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-seismicroll@1.1:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
