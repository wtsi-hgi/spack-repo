# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZlavian(RPackage):
	"""Zipf's Law of Abbreviation in Animal Vocalisations

	Assesses evidence for Zipf's Law of Abbreviation in animal vocalisation using IDs, note class and note duration. The package also provides a webplot function for visualisation. Davis, M. K., and Chen, G. (2007) <doi:10.2307/2346786>.
	"""
	
	homepage = "https://github.com/CDr-er/ZLAvian"
	cran = "ZLAvian" 

	version("0.1.0", md5="658b333edf5ffd56b50c2b6e6065fef1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-lme4@1.1.34:", type=("build", "run"))
	depends_on("r-performance@0.10.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
