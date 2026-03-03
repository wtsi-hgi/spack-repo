# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcdk(RPackage):
	"""Interface to the 'CDK' Libraries

	Allows the user to access functionality in the
    'CDK', a Java framework for chemoinformatics. This allows the user to load
    molecules, evaluate fingerprints, calculate molecular descriptors and so on.
    In addition, the 'CDK' API allows the user to view structures in 2D.
	"""
	
	cran = "rcdk" 

	version("3.8.1", md5="0637f767c703e43686f9b02e5f33196c")

	depends_on("r-rcdklibs@2.8:", type=("build", "run"))
	depends_on("r-fingerprint", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
