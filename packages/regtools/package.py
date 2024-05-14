# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Regtools(CMakePackage):
    """Tools that integrate DNA-seq and RNA-seq data to help interpret mutations in a regulatory and splicing context."""

    homepage = "https://regtools.readthedocs.io/"
    url = "https://github.com/griffithlab/regtools/archive/refs/tags/1.0.0.tar.gz"

    version("1.0.0", sha256="ed2b9db6b71b943924002653caee18511a22ed7cc3c88f428e7e9e0c2e4f431b")
    version("0.5.2", sha256="24d3bc18174237e0fc2d0330839c8dc21c97cdb7d6e528c518188c10f17f3e7e")
    version("0.5.1", sha256="ab6237d9c8fa69f1eb25dbac9383c06ffa9de9fef073269c20ccd89e6f542fbf")
    version("0.5.0", sha256="c9a5f05b23ffb219c35d12a0403b34db7f7cee2b0be7dc3b6f71154dc838917e")
    version("0.4.2", sha256="47b52015c4d36d064f1ebf36c8481f6119b9e993df3c078d1e2925c45d2e72d0")

    depends_on("zlib", type=("build", "link"))

    def install(self, spec, prefix):
        mkdir("build")
        cd("build")
        cmake("..")
        make()
        mkdir(prefix.bin)
        install("regtools", prefix.bin)
