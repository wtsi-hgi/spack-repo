# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesdatras(RPackage):
	"""DATRAS Trawl Survey Database Web Services

	R interface to access the web services of the ICES (International
             Council for the Exploration of the Sea) DATRAS trawl survey
             database <https://datras.ices.dk/WebServices/Webservices.aspx>.
	"""
	
	homepage = "https://datras.ices.dk/WebServices/Webservices.aspx"
	cran = "icesDatras" 

	version("1.4.1", md5="b7ec22082fe2c9f0e81f4cce2af43d78")

