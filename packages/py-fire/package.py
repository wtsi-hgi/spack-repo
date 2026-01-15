# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyFire(Package):
    """FIRE is a Snakemake workflow and training toolkit for Fiber-seq
    based inference of regulatory elements."""

    homepage = "https://github.com/fiberseq/FIRE"
    url = "https://github.com/fiberseq/FIRE/archive/refs/tags/v0.1.3.tar.gz"

    license("MIT")

    version("0.1.3", sha256="dea5dfd53dc33d445b948c8521cd73e4088dcc642c6bf01e02258928b7a4ef41")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-defopt@7:", type="run")
    depends_on("py-mokapot@0.10.0:", type="run")
    depends_on("py-xgboost@1.6.1:+plotting+scikit-learn", type="run")
    depends_on("py-pandas@1.4:1.5", type="run")
    depends_on("py-numpy@1.24:1", type="run")
    depends_on("py-scikit-learn@1.2:", type="run")
    depends_on("py-matplotlib@3.6:", type="run")

    def install(self, spec, prefix):
        sharedir = join_path(prefix.share, "py-fire")
        install_tree(".", sharedir)

        train_dir = join_path(sharedir, "Train-FIRE-v2.0")
        train_script = join_path(train_dir, "train-fire-model.py")
        bindir = prefix.bin
        mkdirp(bindir)

        wrapper = join_path(bindir, "fire-train")
        python_exe = self.spec["python"].command.path
        with open(wrapper, "w", encoding="utf-8") as fh:
            fh.write("#!/bin/bash\n")
            fh.write("set -euo pipefail\n")
            fh.write(f'export PY_FIRE_HOME="{sharedir}"\n')
            fh.write(f'export PY_FIRE_TRAIN_DIR="{train_dir}"\n')
            fh.write(f'exec "{python_exe}" "{train_script}" "$@"\n')
        os.chmod(wrapper, 0o755)

    def setup_run_environment(self, env):
        sharedir = join_path(self.prefix.share, "py-fire")
        env.set("PY_FIRE_HOME", sharedir)
        env.set("PY_FIRE_TRAIN_DIR", join_path(sharedir, "Train-FIRE-v2.0"))

    @run_after("install")
    def install_test(self):
        self.run_test(
            join_path(self.prefix.bin, "fire-train"),
            ["--help"],
            purpose="Ensure the FIRE training CLI is available",
        )
