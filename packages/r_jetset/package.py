# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJetset(RPackage):
	"""One-to-One Gene-Probeset Mapping for Affymetrix Human
Microarrays

	On Affymetrix gene expression microarrays, a single gene may be measured by multiple probe sets. This can present a mild conundrum when attempting to evaluate a gene "signature" that is defined by gene names rather than by specific probe sets. This package provides a one-to-one mapping from gene to "best" probe set for four Affymetrix human gene expression microarrays: hgu95av2, hgu133a, hgu133plus2, and u133x3p. This package also includes the pre-calculated probe set quality scores that were used to define the mapping.
	"""
	
	homepage = "http://www.cbs.dtu.dk/biotools/jetset/"
	cran = "jetset" 

	version("3.4.0", md5="0cd45e49184a6fabea78d8562789e454")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
