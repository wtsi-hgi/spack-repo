# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIced(RPackage):
	"""IntraClass Effect Decomposition

	Estimate test-retest reliability for complex sampling strategies 
    and extract variances using IntraClass Effect Decomposition. Developed by
    Brandmaier et al. (2018) "Assessing reliability in neuroimaging research through intra-class effect decomposition (ICED)" <doi:10.7554/eLife.35718> 
    Also includes functions to simulate data based on sampling strategy. 
    Unofficial version release name: "Good work squirrels".
	"""
	
	homepage = "https://github.com/sdparsons/ICED"
	cran = "ICED" 

	version("0.0.1", md5="c2d40f6fbfad3364a94f692603f6cbb9")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
