# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosmicsig(RPackage):
	"""Mutational Signatures from COSMIC (Catalogue of Somatic
Mutations in Cancer)

	A data package with 2 main package variables: 'signature' and 'etiology'. 
     The 'signature' variable contains the latest mutational signature profiles 
     released on COSMIC <https://cancer.sanger.ac.uk/signatures/> for 3 mutation
     types:
     * Single base substitutions in the context of preceding and following bases,
     * Doublet base substitutions, and
     * Small insertions and deletions.
    The 'etiology' variable provides the known or hypothesized causes of signatures. 
    'cosmicsig' stands for COSMIC signatures. Please run ?'cosmicsig' for more
    information.
	"""
	
	homepage = "https://github.com/Rozen-Lab/cosmicsig"
	cran = "cosmicsig" 

	version("1.1.1", md5="2fbcec24e872af479fa8d9ac7a6c3f59")

	depends_on("r@3.5:", type=("build", "run"))
