# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperimenthubdata(RPackage):
	"""Add resources to ExperimentHub

	Functions to add metadata to ExperimentHub db and resource files to AWS S3 buckets.
	"""
	
	bioc = "ExperimentHubData"

	version("1.34.0", commit="2e8746ac8b2d7da7a9b05bfa6ed3d912621b45bc")
	version("1.28.0", commit="ac4c327cc05effc76f406c8339da8972133bf48d")

	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-annotationhubdata@1.21.3:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
