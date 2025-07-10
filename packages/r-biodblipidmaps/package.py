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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodbLipidmaps_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodbLipidmaps/biodbLipidmaps_1.8.0.tar.gz"]

	version("1.8.0", sha256="ba97d2b5411ff4e261201bf24740d7f07a201478f7f995c400bfde123347ff83")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
