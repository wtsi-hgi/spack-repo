# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Librmm(CMakePackage):
    """RMM: RAPIDS Memory Manager. Achieving optimal
    performance in GPU-centric workflows frequently requires
    customizing how host and device memory are allocated."""

    homepage = "https://github.com/rapidsai/rmm"
    url = "https://github.com/rapidsai/rmm/archive/v0.15.0.tar.gz"

    license("Apache-2.0")
    
    version("24.06.00", sha256="b7300c337b0c9a335e3386f88d6a39ed3eb8d3f66be1330ae2492c862d47aa32")
    version("24.04.00", sha256="bb20877c8d92b322dbcb348c2009040784189d3d3c48f93011e13c1b34f6a22f")
    version("24.02.00", sha256="63ddde8788727f0989f6397aed8a007ef414a577417b7d3cf39ca670c1bc4a91")
    version("0.15.0", sha256="599f97b95d169a90d11296814763f7e151a8a1e060ba10bc6c8f4684a5cd7972")

    # depends_on("cxx", type="build")  # generated

    depends_on("cuda@9.0:")

    def patch(self):
        filter_file("#include <vector>", """#include <vector>
    #include <limits>""", "benchmarks/utilities/rapidcsv.h", string=True)