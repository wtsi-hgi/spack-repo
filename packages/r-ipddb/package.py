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

	version("1.26.0", commit="2c0158285b7196f2b0e9a9668c339f91922eab14")
	version("1.20.0", commit="91c41ad259a2d808ca2f5a17e335e31c3d920c4b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi@1.43.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
