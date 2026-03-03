# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeno2proteo(RPackage):
	"""Finding the DNA and Protein Sequences of Any Genomic or
Proteomic Loci

	Using the DNA sequence and gene annotation files provided in 
            'ENSEMBL' <https://www.ensembl.org/index.html>, 
            the functions implemented in the package try to find the DNA sequences and 
            protein sequences of any given genomic loci, and to find the genomic coordinates 
            and protein sequences of any given protein locations, which are the frequent
            tasks in the analysis of genomic and proteomic data.
	"""
	
	cran = "geno2proteo" 

	version("0.0.6", md5="62e6fc67a52b68da5953c762b028fbc2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("perl@2.0.0:", type=("build", "link", "run"))
