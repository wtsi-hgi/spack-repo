# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSojournData(RPackage):
	"""Supporting Objects for Sojourn Accelerometer Methods

	Stores objects (e.g. neural networks) that are needed for
    using Sojourn accelerometer methods. For more information, see
    Lyden K, Keadle S, Staudenmayer J, & Freedson P (2014)
    <doi:10.1249/MSS.0b013e3182a42a2d>, Ellingson LD, Schwabacher IJ,
    Kim Y, Welk GJ, & Cook DB (2016) <doi:10.1249/MSS.0000000000000915>,
    and Hibbing PR, Ellingson LD, Dixon PM, & Welk GJ (2018)
    <doi:10.1249/MSS.0000000000001486>.
	"""
	
	homepage = "https://github.com/paulhibbing/Sojourn.Data"
	cran = "Sojourn.Data" 

	version("0.3.0", md5="c3e8a985d9702101e4961a108e80a67a")

	depends_on("r@3.1:", type=("build", "run"))
