# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerbalisr(RPackage):
	"""Describe Pedigree Relationships in Words

	Describe in words the genealogical relationship between two
    members of a given pedigree. 'verbalisr' is part of the 'ped suite'
    collection of packages for pedigree analysis. For a demonstration of
    'verbalisr', see the online app 'QuickPed' at
    <https://magnusdv.shinyapps.io/quickped>.
	"""
	
	homepage = "https://github.com/magnusdv/verbalisr"
	cran = "verbalisr" 

	version("0.5.1", md5="ad102eb27866902f758d9b2356f2f2c5")

	depends_on("r-pedtools@2.2:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ribd@1.5:", type=("build", "run"))
