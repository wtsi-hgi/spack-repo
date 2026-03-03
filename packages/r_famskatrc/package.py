# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamskatrc(RPackage):
	"""Family Sequence Kernel Association Test for Rare and Common
Variants

	FamSKAT-RC is a family-based association kernel test for both 
    rare and common variants. This test is general and several special cases 
    are known as other methods: famSKAT, which only focuses on rare variants 
    in family-based data, SKAT, which focuses on rare variants in 
    population-based data (unrelated individuals), and SKAT-RC, which focuses 
    on both rare and common variants in population-based data. When one 
    applies famSKAT-RC and sets the value of phi to 1, famSKAT-RC becomes 
    famSKAT. When one applies famSKAT-RC and set the value of phi to 1 and the 
    kinship matrix to the identity matrix, famSKAT-RC becomes SKAT. When one 
    applies famSKAT-RC and set the kinship matrix (fullkins) to the identity 
    matrix (and phi is not equal to 1), famSKAT-RC becomes SKAT-RC. We also 
    include a small sample synthetic pedigree to demonstrate the method with.  
    For more details see Saad M and Wijsman EM (2014) <doi:10.1002/gepi.21844>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "famSKATRC" 

	version("1.1.0", md5="0d7ad8c82e0809f2149babcb70b3c16d")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
