# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChaos01(RPackage):
	"""0-1 Test for Chaos

	Computes and visualize the results of the 0-1 test for chaos proposed
    by Gottwald and Melbourne (2004) <DOI:10.1137/080718851>. The algorithm is
    available in parallel for the independent values of parameter c. Additionally,
    fast RQA is added to distinguish chaos from noise.
	"""
	
	homepage = "https://code.it4i.cz/ADAS/Chaos01"
	cran = "Chaos01" 

	version("1.2.1", md5="530dc3db9e71e6cac9515b380092319a", url="https://cran.r-project.org/src/contrib/Chaos01_1.2.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
