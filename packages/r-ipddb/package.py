# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpddb(RPackage):
	"""IPD IMGT/HLA and IPD KIR database for Homo sapiens

	All alleles from the IPD IMGT/HLA <https://www.ebi.ac.uk/ipd/imgt/hla/> and IPD KIR <https://www.ebi.ac.uk/ipd/kir/> database for Homo sapiens. Reference: Robinson J, Maccari G, Marsh SGE, Walter L, Blokhuis J, Bimber B, Parham P, De Groot NG, Bontrop RE, Guethlein LA, and Hammond JA KIR Nomenclature in non-human species Immunogenetics (2018), in preparation.
	"""
	
	homepage = "https://github.com/DKMS-LSL/ipdDb"
	bioc = "ipdDb" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ipdDb_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ipdDb/ipdDb_1.20.0.tar.gz"]

	version("1.20.0", sha256="5585cff787a7fb7ce37aba97aa052ef074b2723e5176d289e4d2284e2310a096")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi@1.43.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
