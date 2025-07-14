# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGotools(RPackage):
	"""Functions for Gene Ontology database

	Wraper functions for description/comparison of oligo ID list using Gene Ontology database
	"""
	
	bioc = "goTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/goTools_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/goTools/goTools_1.76.0.tar.gz"]

	version("1.82.0", tag="RELEASE_3_21")
	version("1.76.0", sha256="6c9bc2f6ede0df75c4181ad54434835027f8e1a72e60539a3d34f37f8221d4e1")

	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
