# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObjectproperties(RPackage):
	"""A Factory of Self-Describing Properties

	Supports the definition of sets of properties on objects. Observers can listen to changes on individual properties or the set as a whole. The properties are meant to be fully self-describing. In support of this, there is a framework for defining enumerated types, as well as other bounded types, as S4 classes.
	"""
	
	cran = "objectProperties" 

	version("0.6.8", md5="18c1e4e7b82e94ac187d1120c7125c83")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-objectsignals@0.10.2:", type=("build", "run"))
