# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodblipidmaps(RPackage):
	"""biodbLipidmaps, a library for connecting to the Lipidmaps Structure database

	The biodbLipidmaps library provides access to the Lipidmaps Structure Database, using biodb package framework. It allows to retrieve entries by their accession number, and run web the services lmsdSearch and lmsdRecord.
	"""
	
	homepage = "https://github.com/pkrog/biodbLipidmaps"
	bioc = "biodbLipidmaps"

	version("1.8.0", commit="f02eeddaedd837dd55fd1198e813f8eaea48b3be")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
