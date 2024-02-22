# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrex(RPackage):
	"""Gene ID Mapping for Genotype-Tissue Expression (GTEx) Data

	Convert 'Ensembl' gene identifiers from Genotype-Tissue
    Expression (GTEx) data to identifiers in other annotation systems,
    including 'Entrez', 'HGNC', and 'UniProt'.
	"""
	
	homepage = "https://nanx.me/grex/"
	cran = "grex" 

	version("1.9", md5="a05624a5cee105ca306c405d23752da0")

	depends_on("r@3.5:", type=("build", "run"))
