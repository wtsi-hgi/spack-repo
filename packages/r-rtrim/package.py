# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrim(RPackage):
	"""Trends and Indices for Monitoring Data

	The TRIM model is widely used for estimating growth and decline of
    animal populations based on (possibly sparsely available) count data. The
    current package is a reimplementation of the original TRIM software developed
    at Statistics Netherlands by Jeroen Pannekoek. See
    <https://www.cbs.nl/en-gb/society/nature-and-environment/indices-and-trends%2d%2dtrim%2d%2d>
    for more information about TRIM.
	"""
	
	homepage = "https://github.com/markvanderloo/rtrim"
	cran = "rtrim" 

	version("2.1.1", md5="432c3e42dd89beb210648986a46c6e4b")

