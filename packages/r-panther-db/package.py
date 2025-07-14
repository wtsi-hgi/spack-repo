# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPantherDb(RPackage):
	"""A set of annotation maps describing the entire PANTHER Gene Ontology

	A set of annotation maps describing the entire Gene Ontology assembled using data from PANTHER.
	"""
	
	bioc = "PANTHER.db"

	version("1.0.12", commit="4549c6bff4f28a4bc3559413c9d58235bdad768d")
	version("1.0.12", commit="4549c6bff4f28a4bc3559413c9d58235bdad768d")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-biocfilecache@1.10.1:", type=("build", "run"))

