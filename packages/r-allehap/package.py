# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllehap(RPackage):
	"""Allele Imputation and Haplotype Reconstruction from Pedigree
Databases

	Tools to simulate alphanumeric alleles, impute genetic missing data and reconstruct non-recombinant haplotypes from pedigree databases in a deterministic way. Allelic simulations can be implemented taking into account many factors (such as number of families, markers, alleles per marker,
    probability and proportion of missing genotypes, recombination rate, etc).
    Genotype imputation can be used with simulated datasets or real databases (previously loaded in .ped format). Haplotype reconstruction can be carried
    out even with missing data, since the program firstly imputes each family genotype (without a reference panel), to later reconstruct the corresponding
    haplotypes for each family member. All this considering that each individual (due to meiosis) should unequivocally have two alleles per marker (one inherited
    from each parent) and thus imputation and reconstruction results can be deterministically calculated.
	"""
	
	cran = "alleHap" 

	version("0.9.9", md5="19008754e4b4a32ff96c53f5e3e5b4af")

	depends_on("r-abind", type=("build", "run"))
