# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfilescoredist(RPackage):
	"""Profile score distributions

	Regularization and score distributions for position count matrices.
	"""
	
	bioc = "profileScoreDist" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/profileScoreDist_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/profileScoreDist/profileScoreDist_1.30.0.tar.gz"]

	version("1.30.0", sha256="9a57ec2bb91b13a477087119eb7f541d97d4d7d0027e73b10deb977616ae64f4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
