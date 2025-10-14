# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mosdepth(Package):
    """
    Fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing.
    Installs the upstream static binary from GitHub releases.
    """

    homepage = "https://github.com/brentp/mosdepth"
    url = "https://github.com/brentp/mosdepth/releases/download/v0.3.11/mosdepth"

    license("MIT")

    # Upstream provides a static Linux binary. Use binary asset directly.
    version(
        "0.3.11",
        sha256="4564b69249f03cb5ccb2bb04a8b4723293c86b9c9183cf40c50711e5003cdef2",
        expand=False,
    )

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        # Stage contains the downloaded binary named 'mosdepth'
        install(join_path(self.stage.source_path, "mosdepth"), prefix.bin.mosdepth)
        # Ensure executable bit is set
        chmod = which("chmod")
        chmod("+x", prefix.bin.mosdepth)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # CLI exists; verify it responds
            Executable(join_path(self.prefix.bin, "mosdepth"))("--help")

