# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProsetta(RPackage):
	"""Linking Patient-Reported Outcomes Measures

	Perform scale linking to establish relationships between instruments
    that measure similar constructs according to the PROsetta Stone methodology, as in Choi, Schalet, Cook, & Cella (2014) <doi:10.1037/a0035768>.
	"""
	
	homepage = "https://www.prosettastone.org/"
	cran = "PROsetta" 

	version("0.4.1", md5="c913dcd630f4b8c060153609179ca9e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-equate", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-plink", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-testdesign@1.5.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
