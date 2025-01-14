# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class CnsSolve(Package):
    """Crystallography & NMR System Solve."""

    homepage = "http://cns-online.org/v1.21/"
    git = "https://gitlab.internal.sanger.ac.uk/eh19/cnssolve"

    version("1.21", tag="1.21-bin")

    def install(self, spec, prefix):
        tar = which("tar")
        tar("-xzf", f"cns_solve_{self.version}_all_intel-mac_linux-mp.tar.gz")
        mkdirp(prefix.bin)
        install(f"cns_solve_{self.version}/intel-x86_64bit-linux/source/*.exe", prefix.bin.cns_solve)
