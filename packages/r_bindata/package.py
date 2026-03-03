# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBindata(RPackage):
	"""Generation of Artificial Binary Data

	Generation of correlated artificial binary data.
	"""
	
	cran = "bindata" 

	version("0.9-20", md5="ed849928433cc36e69841b944eb41b58")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mvtnorm@0.7.0:", type=("build", "run"))
