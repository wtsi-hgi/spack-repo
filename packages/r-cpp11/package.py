# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpp11(RPackage):
    """A C++11 Interface for R's C Interface
    
    Provides a header only, C++11 interface to R's C interface. Compared to other approaches 'cpp11' strives to be safe against long jumps from the C API as well as C++ exceptions, conform to normal R function semantics and supports interaction with 'ALTREP' vectors.
    """

    homepage = "https://cpp11.r-lib.org"
    cran = "cpp11"

    version("0.4.6", sha256="d1c56954671d3398078ad52aaa4efce0864e8166465c8c5e5e9a1e40599055b3")

