# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSewage(RPackage):
	"""A Light-Weight Data Pipelining Tool

	Provides a simple interface to developing complex data pipelines which can be executed in a single call.
    'sewage' makes it easy to test, debug, and share data pipelines through it's interface and visualizations.
	"""
	
	homepage = "https://github.com/mwhalen18/sewage"
	cran = "sewage" 

	version("0.2.5", md5="16ceddc8beece9351079be209f42cb54")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
