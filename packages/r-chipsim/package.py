# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipsim(RPackage):
	"""Simulation of ChIP-seq experiments

	A general framework for the simulation of ChIP-seq data. Although currently focused on nucleosome positioning the package is designed to support different types of experiments.
	"""
	
	bioc = "ChIPsim" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChIPsim_1.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChIPsim/ChIPsim_1.56.0.tar.gz"]

	version("1.56.0", md5="e6f1bd9d18f542abace1039c37ada326")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
