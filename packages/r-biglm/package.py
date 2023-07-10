# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiglm(RPackage):
    """Bounded Memory Linear and Generalized Linear Models
    
    Regression for data too large to fit in memory.
    """

    homepage = "https://cran.r-project.org/web/packages/biglm"
    
    cran = "biglm"

    # versions
    version("0.9-2.1", md5="6f358d6fc78c251b7737e4c0206175fb")
    

    # dependencies
    
