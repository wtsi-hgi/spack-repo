# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfishbc(RPackage):
	"""Back-Calculation of Fish Length

	Helps fisheries scientists collect measurements from calcified
    structures and back-calculate estimated lengths at previous ages using
    standard procedures and models. This is intended to replace much of the
    functionality provided by the now out-dated 'fishBC' software
    (<https://fisheries.org/bookstore/all-titles/software/70317/>).
	"""
	
	homepage = "https://fishr-core-team.github.io/RFishBC/"
	cran = "RFishBC" 

	version("0.2.7", md5="2e9e5dc6e153a80967902de3bcc7b0c1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
