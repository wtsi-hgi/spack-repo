# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContactdata(RPackage):
	"""Social Contact Matrices for 177 Countries

	Data package for the supplementary data in Prem et al. (2017)
    <doi:10.1371/journal.pcbi.1005697> and Prem et al. 
    <doi:10.1371/journal.pcbi.1009098>.
    Provides easy access to contact data for 177 countries, for use in
    epidemiological, demographic or social sciences research.
	"""
	
	homepage = "https://hugogruson.fr/contactdata/"
	cran = "contactdata" 

	version("1.0.0", md5="f0ac7a275e29bdd5f649c7ad51dd79e1")

	depends_on("r@3.5:", type=("build", "run"))
