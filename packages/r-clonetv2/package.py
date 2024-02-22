# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClonetv2(RPackage):
	"""Clonality Estimates in Tumor

	Analyze data from next-generation sequencing experiments on genomic samples. 'CLONETv2' offers a set of functions to compute allele specific copy number and clonality from segmented data and SNPs position pileup. The package has also calculated the clonality of single nucleotide variants given read counts at mutated positions. The package has been developed at the laboratory of Computational and Functional Oncology, Department of CIBIO, University of Trento (Italy), under the supervision of prof Francesca Demichelis. References: Prandi et al. (2014) <doi:10.1186/s13059-014-0439-6>; Carreira et al. (2014) <doi:10.1126/scitranslmed.3009448>; Romanel et al. (2015) <doi:10.1126/scitranslmed.aac9511>.
	"""
	
	cran = "CLONETv2" 

	version("2.2.1", md5="a1b4890c254a97be5eeca428b16abb3f", url="https://cran.r-project.org/src/contrib/CLONETv2_2.2.1.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
