# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrodatoses(RPackage):
	"""Utilities for Official Spanish Microdata

	Provides utilities for reading and processing microdata from Spanish official statistics with R.
	"""
	
	homepage = "https://www.datanalytics.com/2012/08/06/un-paseo-por-el-paquete-microdatoses-y-la-epa-de-nuevo/"
	cran = "MicroDatosEs" 

	version("0.8.15", md5="0c3bdaac21e6aa73553f665453497ea1")

	depends_on("r-readr", type=("build", "run"))
