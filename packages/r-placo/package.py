# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from glob import glob

from spack.package import *
from spack.util.executable import Executable


class RPlaco(Package):
    """PLACO provides pleiotropic association tests for two traits from GWAS
    summary statistics, including the PLACO+ test that accounts for correlated
    traits."""

    homepage = "https://github.com/RayDebashree/PLACO"
    git = "https://github.com/RayDebashree/PLACO.git"

    license("GPL-3.0-or-later")

    version("20250918", commit="3ba3cae1d323ad117fb4540e620bcefa79f70663")

    depends_on("r@3.0.1:", type=("build", "run"))

    def install(self, spec, prefix):
        script_candidates = sorted(
            f for f in glob("PLACO_v*.R") if "_example" not in f.lower()
        )
        if not script_candidates:
            raise InstallError("PLACO script not found in staging area")

        share_dir = join_path(prefix.share, "r-placo")
        mkdirp(share_dir)

        script_dst = join_path(share_dir, "placo.R")
        install(script_candidates[-1], script_dst)

        optional_artifacts = [
            "README.md",
            "PLACO_v0.2.0_example.R",
            "PLACO_v0.2.0_manual.pdf",
        ]
        for artifact in optional_artifacts:
            if os.path.exists(artifact):
                install(artifact, join_path(share_dir, os.path.basename(artifact)))

        if os.path.exists("LICENSE"):
            install("LICENSE", join_path(prefix, "LICENSE"))

        self._installed_script = script_dst

    @run_after("install")
    def install_test(self):
        if not self.run_tests:
            return

        script_path = getattr(
            self, "_installed_script", join_path(self.prefix.share, "r-placo", "placo.R")
        )
        script_path_escaped = script_path.replace('"', '\\"')
        rscript = Executable(join_path(self.spec["r"].prefix.bin, "Rscript"))
        rscript(
            "-e",
            'source("{0}"); stopifnot(is.function(placo)); stopifnot(is.function(placo.plus))'.format(
                script_path_escaped
            ),
        )
