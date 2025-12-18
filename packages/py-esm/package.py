# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEsm(PythonPackage):
    """EvolutionaryScale open model repository."""

    homepage = "https://github.com/evolutionaryscale/esm"
    pypi = "esm/esm-3.2.3-py3-none-any.whl"

    version(
        "3.2.3",
        sha256="61847d25b80efe0121931609b5ea885cc142ceb8caaa22ead6e3e97c527bc2af",
        expand=False,
        url="https://files.pythonhosted.org/packages/b9/e6/d2ac74ec2ad695073ca49f0e9887ce9c47302578af05dbe39b099a7c0af5/esm-3.2.3-py3-none-any.whl",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("python@3.12:3.12", type=("build", "run"))

    depends_on("py-attrs", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-biotite@1.0.0:", type=("build", "run"))
    depends_on("py-boto3", type=("build", "run"))
    depends_on("py-brotli", type=("build", "run"))
    depends_on("py-cloudpathlib", type=("build", "run"))
    depends_on("py-dna-features-viewer", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-httpx", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-ipywidgets", type=("build", "run"))
    depends_on("py-msgpack-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-py3dmol", type=("build", "run"))
    depends_on("py-pydssp", type=("build", "run"))
    depends_on("py-pygtrie", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-tenacity", type=("build", "run"))
    depends_on("py-torch@2.2.0:", type=("build", "run"))
    depends_on("py-torchtext", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-transformers@:4.48.1", type=("build", "run"))
    depends_on("py-zstd", type=("build", "run"))

    def install(self, spec, prefix):
        from spack.build_systems.python import PythonPipBuilder

        wheel_path = self.stage.archive_file
        pip(*PythonPipBuilder.std_args(self), f"--prefix={prefix}", wheel_path)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import esm; print(esm.__version__)")
