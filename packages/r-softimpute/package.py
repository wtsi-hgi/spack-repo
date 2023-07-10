# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoftimpute(RPackage):
    """Matrix Completion via Iterative Soft-Thresholded SVD
    
    Iterative methods for matrix completion that use nuclear-norm regularization. There are two main approaches.The one approach uses iterative soft-thresholded svds to impute the missing values. The second approach uses alternating least squares. Both have an 'EM' flavor, in that at each iteration the matrix is completed with the current estimate. For large matrices there is a special sparse-matrix class named "Incomplete" that efficiently handles all computations. The package includes procedures for centering and scaling rows, columns or both, and for computing low-rank SVDs on large sparse centered matrices (i.e. principal components).
    """

    homepage = "https://cran.r-project.org/web/packages/softImpute"
    
    cran = "softImpute"

    # versions
    version("1.4-1", md5="a17b4aafe9961e6af8f7808829459e90")
    

    # dependencies
    
