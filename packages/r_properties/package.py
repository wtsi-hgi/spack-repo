# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProperties(RPackage):
	"""Parse 'Java' Properties Files for 'R Service Bus' Applications

	Allows to parse 'Java' properties files in the context of
  'R Service Bus' applications.
	"""
	
	homepage = "https://www.rservicebus.io/"
	cran = "properties" 

	version("0.0-9", md5="de696d506f435e040f0b215da4d3c643")

