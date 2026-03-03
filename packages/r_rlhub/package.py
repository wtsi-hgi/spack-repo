# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlhub(RPackage):
	"""RLHub (part of RLSuite) provides easy access to the processed R-loop mapping data stored in RLBase. It is an ExperimentHub package with built-in accessors that streamline the data retrieval process."""
	
	homepage = "https://github.com/Bishop-Laboratory/RLHub"
	git = "https://github.com/Bishop-Laboratory/RLHub.git" 

	version("2022-01-20", commit="f0e67e20ddc2e4e000e04cd79e2304824e41720a")

	depends_on("r-annotationhub", type=("build", "link", "run"))
	depends_on("r-experimenthub", type=("build", "link", "run"))
