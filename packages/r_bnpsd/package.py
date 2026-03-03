# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnpsd(RPackage):
	"""Simulate Genotypes from the BN-PSD Admixture Model

	The Pritchard-Stephens-Donnelly (PSD) admixture model has k intermediate subpopulations from which n individuals draw their alleles dictated by their individual-specific admixture proportions.  The BN-PSD model additionally imposes the Balding-Nichols (BN) allele frequency model to the intermediate populations, which therefore evolved independently from a common ancestral population T with subpopulation-specific FST (Wright's fixation index) parameters.  The BN-PSD model can be used to yield complex population structures.  This simulation approach is now extended to subpopulations related by a tree.  Method described in Ochoa and Storey (2021) <doi:10.1371/journal.pgen.1009241>.
	"""
	
	homepage = "https://github.com/StoreyLab/bnpsd/"
	cran = "bnpsd" 

	version("1.3.13", md5="9c242be61ef5a7ef23a25a044341aa83")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
