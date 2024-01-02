# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RProfmem(RPackage):
    """Simple Memory Profiling for R
    
    A simple and light-weight API for memory profiling of R expressions. The profiling is built on top of R's built-in memory profiler ('utils::Rprofmem()'), which records every memory allocation done by R (also native code).
    """

    homepage = "https://github.com/HenrikBengtsson/profmem"
    cran = "profmem"

    version("0.6.0", sha256="745ca9b22a8de3cda4374be6e2454e549742a3b72ff02c8894c972178192e63d")