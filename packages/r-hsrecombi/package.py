# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsrecombi(RPackage):
	"""Estimation of Recombination Rate and Maternal LD in Half-Sibs

	Paternal recombination rate and maternal linkage disequilibrium 
    (LD) are estimated for pairs of biallelic markers such as single nucleotide 
    polymorphisms (SNPs) from progeny genotypes and sire haplotypes. The 
    implementation relies on paternal half-sib families. If maternal half-sib 
    families are used, the roles of sire/dam are swapped. Multiple families can 
    be considered. For parameter estimation, at least one sire has to be double 
    heterozygous at the investigated pairs of SNPs.
    Based on recombination rates, genetic distances between markers can be 
    estimated. Markers with unusually large recombination rate to markers in 
    close proximity (i.e. putatively misplaced markers) shall be discarded in 
    this derivation.
    A workflow description is attached as vignette.
    *A pipeline is available at GitHub*
    <https://github.com/wittenburg/hsrecombi>
    Hampel, Teuscher, Gomez-Raya, Doschoris, Wittenburg (2018) "Estimation of 
    recombination rate and maternal linkage disequilibrium in half-sibs" 
    <doi:10.3389/fgene.2018.00186>.
    Gomez-Raya (2012) "Maximum likelihood estimation of linkage disequilibrium 
    in half-sib families" <doi:10.1534/genetics.111.137521>.
	"""
	
	cran = "hsrecombi" 

	version("1.0.1", md5="d937eb56061ea1fc7b684cfc5e54b970")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hsphase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
