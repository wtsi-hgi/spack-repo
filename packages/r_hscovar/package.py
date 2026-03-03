# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHscovar(RPackage):
	"""Calculation of Covariance Between Markers for Half-Sib Families

	The theoretical covariance between pairs of markers is calculated
    from either paternal haplotypes and maternal linkage disequilibrium (LD) or 
    vise versa. A genetic map is required. Grouping of markers is based on the 
    correlation matrix and a representative marker is suggested for each group.
    Employing the correlation matrix, optimal sample size can be derived for 
    association studies based on a SNP-BLUP approach.
    The implementation relies on paternal half-sib families and biallelic 
    markers. If maternal half-sib families are used, the roles of sire/dam are 
    swapped. Multiple families can be considered.
    Wittenburg, Bonk, Doschoris, Reyer (2020) "Design of Experiments for 
    Fine-Mapping Quantitative Trait Loci in Livestock Populations" 
    <doi:10.1186/s12863-020-00871-1>.
    Carlson, Eberle, Rieder, Yi, Kruglyak, Nickerson (2004) "Selecting a 
    maximally informative set of single-nucleotide polymorphisms for association
    analyses using linkage disequilibrium" <doi:10.1086/381000>.
	"""
	
	cran = "hscovar" 

	version("0.4.2", md5="10bf847d6b3559e238c738b554248337")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
