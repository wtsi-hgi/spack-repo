# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

class PyScfea(PythonPackage):
    """A graph neural network model to estimate cell-wise metabolic using single cell RNA-seq data."""

    homepage = "http://scflux.org/"
    url = "https://github.com/changwn/scFEA/archive/refs/tags/v1.1.tar.gz"

    version("1.1", sha256="4a9ec74a85b62dc2fb92c2f32c7faf60d51d8cf88750f9ebdd4b68abfe0d1bb2")
    version("1.0", sha256="d5464a22bfe71c05b385ff5a4ab11cd66bd922a4d4c4a04fcaf59ec52a96ddb3")

    depends_on("py-torch@0.4.1:", type=("build", "run"))
    depends_on("py-numpy@1.15.4:", type=("build", "run"))
    depends_on("py-pandas@0.23.4:", type=("build", "run"))
    depends_on("py-matplotlib@3.0.2:", type=("build", "run"))
    depends_on("py-magic-impute@2.0.4:", type=("build", "run"))
    depends_on("py-tqdm@4.28.1:", type=("build", "run"))
    depends_on("py-umap-learn@0.5.1:", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-graphtools", type="run")
    depends_on("py-deprecated", type="run")
    depends_on("py-future", type="run")
    depends_on("py-scprep", type="run")
    depends_on("py-pygsp", type="run")
    depends_on("py-tasklogger", type="run")

    installDir = "/usr/local/scfeax/"

    def install(self, spec, prefix):
        with open('./src/scFEA.py', 'r') as fh:
            data = fh.read()

        with open('./src/scFEA.py', 'w') as fh:
            fh.write("#!/usr/bin/env python3\n" + data)

        os.chmod("./src/scFEA.py", 0o755)
        mkdirp(prefix + self.installDir)
        install_tree("./src", prefix + self.installDir)

    def setup_run_environment(self, env):
        env.append_path("PATH", self.prefix + self.installDir)

    def setup_dependent_environment(self):
        env.prepend_path("PATH", self.prefix + self.installDir)
