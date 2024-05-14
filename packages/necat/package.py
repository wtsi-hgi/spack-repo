# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import glob

class Necat(Package):
    """NECAT is an error correction and de-novo assembly tool for Nanopore long noisy reads."""

    homepage = "https://github.com/xiaochuanle/NECAT"
    url = "https://github.com/xiaochuanle/NECAT/archive/refs/tags/v0.0.1_update20200803.tar.gz"

    version("0.0.1", sha256="5ddd147b5be6b1fac2f6c10b18c9b587838f2304d2584087c4ed6f628eced06c", url="https://github.com/xiaochuanle/NECAT/archive/refs/tags/v0.0.1_update20200803.tar.gz")
    
    depends_on("perl@5.26.2:", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
    
    def install(self, spec, prefix):
        cd("src")
        make()
        mkdir(prefix.bin)
        install_tree("../Linux-amd64/bin", prefix.bin)

