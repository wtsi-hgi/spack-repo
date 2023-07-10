# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdsmatrix(RPackage):
    """Routines for Block Diagonal Symmetric Matrices
    
    This is a special case of sparse matrices, used by coxme. 
    """

    homepage = "https://cran.r-project.org/web/packages/bdsmatrix"
    
    cran = "bdsmatrix"

    # versions
    version("1.3-6", md5="4f8ccf979ab7f88fa71b7e45323b219a")
    

    # dependencies
    
