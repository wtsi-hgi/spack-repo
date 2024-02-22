# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathifier(RPackage):
	"""Quantify deregulation of pathways in cancer

	Pathifier is an algorithm that infers pathway deregulation scores for each tumor sample on the basis of expression data. This score is determined, in a context-specific manner, for every particular dataset and type of cancer that is being investigated. The algorithm transforms gene-level information into pathway-level information, generating a compact and biologically relevant representation of each sample.
	"""
	
	bioc = "pathifier" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pathifier_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pathifier/pathifier_1.40.0.tar.gz"]

	version("1.40.0", md5="344576d367c4da46c28918be3de3f65e")

	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-princurve@2.0.4:", type=("build", "run"))
