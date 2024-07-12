# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Dorado(CMakePackage):
    """Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads."""

    homepage = "https://nanoporetech.com/"
    git = "https://github.com/nanoporetech/dorado.git"
    submodules = True

    version("0.7.2", tag="v0.7.2")
    version("0.7.1", tag="v0.7.1")
    version("0.7.0", tag="v0.7.0")
    version("0.6.2", tag="v0.6.2")
    version("0.6.1", tag="v0.6.1")
    version("0.6.0", tag="v0.6.0")
    version("0.5.3", tag="v0.5.3")
    version("0.5.2", tag="v0.5.2")
    version("0.5.1", tag="v0.5.1")
    version("0.5.0", tag="v0.5.0")

    depends_on("hdf5", type=("build", "link"))
    depends_on("zlib", type=("build", "link"))
    depends_on("zstd", type=("build", "link"))
    depends_on("libaec", type=("build", "link"))
    depends_on("openssl", type=("build", "link"))
    depends_on("cuda@11.8:", type=("build", "link"))
    depends_on("autoconf", type=("build"))
    depends_on("automake", type=("build"))

    def patch(self):
        with open("dorado/3rdparty/htslib/htscodecs/htscodecs/version.h", "w") as f:
            f.write("#define HTSCODECS_VERSION_TEXT \"1.20\"")
