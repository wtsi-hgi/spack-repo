# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSscu(RPackage):
	"""Strength of Selected Codon Usage

	The package calculates the indexes for selective stength in codon usage in bacteria species. (1) The package can calculate the strength of selected codon usage bias (sscu, also named as s_index) based on Paul Sharp's method. The method take into account of background mutation rate, and focus only on four pairs of codons with universal translational advantages in all bacterial species. Thus the sscu index is comparable among different species. (2) The package can detect the strength of translational accuracy selection by Akashi's test. The test tabulating all codons into four categories with the feature as conserved/variable amino acids and optimal/non-optimal codons. (3) Optimal codon lists (selected codons) can be calculated by either op_highly function (by using the highly expressed genes compared with all genes to identify optimal codons), or op_corre_CodonW/op_corre_NCprime function (by correlative method developed by Hershberg & Petrov). Users will have a list of optimal codons for further analysis, such as input to the Akashi's test. (4) The detailed codon usage information, such as RSCU value, number of optimal codons in the highly/all gene set, as well as the genomic gc3 value, can be calculate by the optimal_codon_statistics and genomic_gc3 function. (5) Furthermore, we added one test function low_frequency_op in the package. The function try to find the low frequency optimal codons, among all the optimal codons identified by the op_highly function.
	"""
	
	bioc = "sscu" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sscu_2.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sscu/sscu_2.32.0.tar.gz"]

    version("2.38.0", tag="RELEASE_3_21")
	version("2.32.0", sha256="a8e11babd13635f20e57d8274522908d6094759b513a55afe902eeac15f75445")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biostrings@2.36.4:", type=("build", "run"))
	depends_on("r-seqinr@3.1.3:", type=("build", "run"))
	depends_on("r-biocgenerics@0.16.1:", type=("build", "run"))
