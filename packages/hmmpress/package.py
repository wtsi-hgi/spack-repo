# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Hmmpress(BundlePackage):
    """Index HMM database files for HMMER. This package provides the
    `hmmpress` CLI by depending on `hmmer` and exposing the binary.

    The `hmmpress` tool is part of the HMMER suite and prepares HMM
    databases for faster searches.
    """

    homepage = "https://biolib.com/HMMER/hmmpress/"

    # Meta version for the bundle; hmmer provides the actual binary
    version("1.0.0")

    # Ensure the HMMER suite is available at runtime
    depends_on("hmmer", type=("build", "run"))

    def install(self, spec, prefix):
        # Expose the hmmpress binary from hmmer under this package prefix
        mkdirp(prefix.bin)
        hmmpress_src = join_path(spec["hmmer"].prefix.bin, "hmmpress")
        if not os.path.exists(hmmpress_src):
            raise InstallError(
                "hmmpress binary not found in hmmer installation: {0}".format(hmmpress_src)
            )
        ln = join_path(prefix.bin, "hmmpress")
        if os.path.islink(ln) or os.path.exists(ln):
            os.remove(ln)
        os.symlink(hmmpress_src, ln)

    @run_after("install")
    def install_test(self):
        # Prefer CLI test; fall back to basic invocation
        with working_dir("spack-test", create=True):
            exe = Executable(join_path(self.prefix.bin, "hmmpress"))
            exe("-h")
