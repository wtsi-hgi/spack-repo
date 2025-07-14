# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetams(RPackage):
	"""MS-based metabolomics annotation pipeline

	MS-based metabolomics data processing and compound annotation pipeline.
	"""
	
	homepage = "https://github.com/yguitton/metaMS"
	bioc = "metaMS"

	version("1.44.0", commit="3aa6f5910127922669890abd152e7a9d54f3858a")
	version("1.38.0", commit="89ef3f2b4c46ca62c6780026d4dd788347117cda")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-xcms@1.35:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
