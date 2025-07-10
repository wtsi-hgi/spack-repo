# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCormotif(RPackage):
	"""Correlation Motif Fit

	It fits correlation motif model to multiple studies to detect study specific differential expression patterns.
	"""
	
	bioc = "Cormotif" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Cormotif_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Cormotif/Cormotif_1.48.0.tar.gz"]

	version("1.48.0", sha256="9bab217df749bc5e40446baef4b1ce9814d27dc55e99d807b581c20f82c87ea9")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
