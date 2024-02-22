# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROryzaprobe(RPackage):
	"""Rice Microarray Probe ID Conversion, from Probe ID to RAP-DB ID

	Microarray probe ID is not convenient for further enrichment analysis and target gene selection.
    The package is created for the rice microarray probe ID conversion.
    This package can convert microarray probe ID from GPL6864 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6864>, GPL8852 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL8852>, and GPL2025 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL2025> platforms to RAP-DB ID. RAP-DB "The Rice Annotation Project Database" <https://rapdb.dna.affrc.go.jp> is a well-known database for rice Oryza sativa, and the gene ID in this database is widely used in many areas related to rice research.
    For multiple probes representing a single gene, This package can merge them by taking the mean, max, or min value of these probes.
    Or we can keep multiple probes by appending sequence numbers to duplicate the RAP-DB ID.
	"""
	
	cran = "OryzaProbe" 

	version("0.1.0", md5="b6d628ccbfad70601e0b54d3666358b4")

	depends_on("r@2.10:", type=("build", "run"))
