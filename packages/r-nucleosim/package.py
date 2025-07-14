# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNucleosim(RPackage):
	"""Generate synthetic nucleosome maps

	This package can generate a synthetic map with reads covering the nucleosome regions as well as a synthetic map with forward and reverse reads emulating next-generation sequencing. The synthetic hybridization data of “Tiling Arrays” can also be generated. The user has choice between three different distributions for the read positioning: Normal, Student and Uniform. In addition, a visualization tool is provided to explore the synthetic nucleosome maps.
	"""
	
	homepage = "https://github.com/arnauddroitlab/nucleoSim"
	bioc = "nucleoSim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nucleoSim_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nucleoSim/nucleoSim_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="efb92f4d9fa84cbedcca21cca593cdbb6008663701707aad76cf197c52b70ea8")

	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
