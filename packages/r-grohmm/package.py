# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrohmm(RPackage):
	"""GRO-seq Analysis Pipeline

	A pipeline for the analysis of GRO-seq data.
	"""
	
	homepage = "https://github.com/Kraus-Lab/groHMM"
	bioc = "groHMM"

	version("1.42.0", commit="bcff43f40bf8a0fa3babec21ffbf503fc8bd3119")
	version("1.36.0", commit="121daf0e3cb0b03b827f777398cb1ecbd55772aa")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
