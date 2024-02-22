# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusteredmutations(RPackage):
	"""Location and Visualization of Clustered Somatic Mutations

	Identification and visualization of groups of closely spaced mutations in the DNA sequence of cancer genome. The extremely mutated zones are searched in the symmetric dissimilarity matrix using the anti-Robinson matrix properties. Different data sets are obtained to describe and plot the clustered mutations information. 
	"""
	
	cran = "ClusteredMutations" 

	version("1.0.1", md5="f1f9a45a53c96681de9f9a7e419b7f8f")

	depends_on("r-seriation", type=("build", "run"))
