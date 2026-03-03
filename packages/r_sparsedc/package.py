# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsedc(RPackage):
	"""Implementation of SparseDC Algorithm

	Implements the algorithm described in 
    Barron, M., Zhang, S. and Li, J. 2017, "A sparse differential
    clustering algorithm for tracing cell type changes via single-cell
    RNA-sequencing data", Nucleic Acids Research, gkx1113,
    <doi:10.1093/nar/gkx1113>. This algorithm clusters samples from two
    different populations, links the clusters across the conditions and
    identifies marker genes for these changes. The package was designed for
    scRNA-Seq data but is also applicable to many other data types, just
    replace cells with samples and genes with variables. The package also
    contains functions for estimating the parameters for SparseDC as outlined
    in the paper. We recommend that users further select their marker genes
    using the magnitude of the cluster centers.
	"""
	
	cran = "SparseDC" 

	version("0.1.17", md5="4db33ecbce87f9b37a9c730b3d8544a4")

	depends_on("r@3.1:", type=("build", "run"))
