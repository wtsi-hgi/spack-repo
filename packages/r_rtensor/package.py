# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtensor(RPackage):
	"""Tools for Tensor Analysis and Decomposition

	A set of tools for creation, manipulation, and modeling
    of tensors with arbitrary number of modes. A tensor in the context of data
    analysis is a multidimensional array. rTensor does this by providing a S4
    class 'Tensor' that wraps around the base 'array' class. rTensor
    provides common tensor operations as methods, including matrix unfolding,
    summing/averaging across modes, calculating the Frobenius norm, and taking
    the inner product between two tensors. Familiar array operations are
    overloaded, such as index subsetting via '[' and element-wise operations.
    rTensor also implements various tensor decomposition, including CP, GLRAM,
    MPCA, PVD, and Tucker. For tensors with 3 modes, rTensor also implements
    transpose, t-product, and t-SVD, as defined in Kilmer et al. (2013). Some
    auxiliary functions include the Khatri-Rao product, Kronecker product, and
    the Hadamard product for a list of matrices.
	"""
	
	homepage = "https://github.com/rikenbit/rTensor"
	cran = "rTensor" 

	version("1.4.8", md5="ef511906da889a60037086dccd717054")

	depends_on("r@2.10:", type=("build", "run"))
