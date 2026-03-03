# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSms(RPackage):
	"""Spatial Microsimulation

	Produce small area population estimates by fitting census data to
    survey data.
	"""
	
	cran = "sms" 

	version("2.3.1", md5="6ba9e07c2f0128077e8c242c623c02d1")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
