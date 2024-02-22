# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDvir(RPackage):
	"""Disaster Victim Identification

	Joint DNA-based disaster victim identification (DVI), as
    described in Vigeland and Egeland (2021)
    <doi:10.21203/rs.3.rs-296414/v1>. Identification is performed by
    optimising the joint likelihood of all victim samples and reference
    individuals. Individual identification probabilities, conditional on
    all available information, are derived from the joint solution in the
    form of posterior pairing probabilities. 'dvir' is part of the
    'pedsuite' collection of packages for pedigree analysis.
	"""
	
	homepage = "https://github.com/magnusdv/dvir"
	cran = "dvir" 

	version("3.2.1", md5="9caf7eaa7c76bc43dbec105bdc8d635f")

	depends_on("r-pedtools@2.4:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-forrel@1.5.2:", type=("build", "run"))
	depends_on("r-pedprobr@0.8:", type=("build", "run"))
	depends_on("r-ribd", type=("build", "run"))
