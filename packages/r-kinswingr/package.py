# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinswingr(RPackage):
	"""KinSwingR: network-based kinase activity prediction

	KinSwingR integrates phosphosite data derived from mass-spectrometry data and kinase-substrate predictions to predict kinase activity. Several functions allow the user to build PWM models of kinase-subtrates, statistically infer PWM:substrate matches, and integrate these data to infer kinase activity.
	"""
	
	bioc = "KinSwingR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/KinSwingR_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/KinSwingR/KinSwingR_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="e5bebe8bde72a0dc89fdca1d742e6f2786f3b5af7949e47604437d4654437e13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
