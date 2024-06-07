# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Pear(Package):
    """PEAR is an ultrafast, memory-efficient and highly accurate pair-end read merger. It is fully parallelized and can run with as low as just a few kilobytes of memory.."""

    homepage = "https://cme.h-its.org/exelixis/web/software/pear/"
    url = "https://depot.galaxyproject.org/software/pear/pear_0.9.11_src_all.tar.gz"

    version("0.9.6", sha256="f7728371e26a5b46fa928b0f7ae1b552ed6a78815b117ba48ef1af98e96c8e2b")

    depends_on("bzip2")
    depends_on("zlib")

    def install(self, spec, prefix):
        configure("--prefix="+prefix)
        make()
        make("install")
