# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmsb(RPackage):
	"""Functions for Medical Statistics Book with some Demographic Data

	Several utility functions for the book entitled 
	"Practices of Medical and Health Data Analysis using R"
	(Pearson Education Japan, 2007) with Japanese demographic
	data and some demographic analysis related functions.
	"""
	
	homepage = "https://minato.sip21c.org/msb/"
	cran = "fmsb" 

	version("0.7.6", md5="281b8f4834c1583168cb0bfd32b58ee2")

	depends_on("r@2.2:", type=("build", "run"))
