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

	version("1.48.0", md5="6e65ec2460aecf6004e416d7c61c4c1d")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
