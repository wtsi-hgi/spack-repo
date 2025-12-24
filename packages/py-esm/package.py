# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEsm(PythonPackage):
    """EvolutionaryScale's open model repository with ESM3 and ESM C tooling."""

    homepage = "https://github.com/evolutionaryscale/esm"
    url = "https://github.com/evolutionaryscale/esm/archive/refs/tags/v3.2.3.tar.gz"
    license("Cambrian-Open-NonCommercial")

    version("3.2.3", sha256="819fd1a7681c965b6ccc1a00ee766940c5c36e3778f2bab393f1d74eb0250853")

    depends_on("python@3.11:3.11", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-torch-gpu@2.2.0:", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-torchtext", type=("build", "run"))
    depends_on("py-transformers@:4.48.1", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-biotite@1.0.0:", type=("build", "run"))
    depends_on("py-msgpack-numpy", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-brotli", type=("build", "run"))
    depends_on("py-attrs", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-cloudpathlib", type=("build", "run"))
    depends_on("py-httpx", type=("build", "run"))
    depends_on("py-tenacity", type=("build", "run"))
    depends_on("py-zstd", type=("build", "run"))
    depends_on("py-ipywidgets", type=("build", "run"))
    depends_on("py-py3dmol", type=("build", "run"))
    depends_on("py-pydssp", type=("build", "run"))
    depends_on("py-boto3", type=("build", "run"))
    depends_on("py-pygtrie", type=("build", "run"))
    depends_on("py-dna-features-viewer", type=("build", "run"))

    def patch(self):
        filter_file(
            'requires-python = ">=3.12,<3.13"',
            'requires-python = ">=3.11,<3.13"',
            "pyproject.toml",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import esm; print(esm.__name__)")
