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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pathifier_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pathifier/pathifier_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="76dd66e9e9690eb73002de1ee4042497c2ef5e94fae202e280d308505a60b078")

	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-princurve@2.0.4:", type=("build", "run"))
