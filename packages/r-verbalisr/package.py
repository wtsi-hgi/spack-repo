# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerbalisr(RPackage):
	"""Describe Pedigree Relationships in Words

	Describe in words the genealogical relationship between two
    members of a given pedigree, using the algorithm in Vigeland (2022)
    <doi:10.1186/s12859-022-04759-y>. 'verbalisr' is part of the
    'pedsuite' collection of packages for pedigree analysis. For a
    demonstration of 'verbalisr', see the online app 'QuickPed' at
    <https://magnusdv.shinyapps.io/quickped>.
	"""
	
	homepage = "https://github.com/magnusdv/verbalisr"
	cran = "verbalisr" 

	version("0.5.2", md5="3ce7e6dea35e3b4b9744d0d8f5750a3e")

	depends_on("r-pedtools@2.2:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ribd@1.5:", type=("build", "run"))
