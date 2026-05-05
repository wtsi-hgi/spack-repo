# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBpnet(PythonPackage):
    """BPNet: toolkit to learn motif synthax from high-resolution functional
    genomics data using convolutional neural networks.
    """

    homepage = "https://github.com/kundajelab/bpnet"
    pypi = "bpnet/bpnet-2.0.0-py3-none-any.whl"

    with default_args(deprecated=True):
        version(
            "0.0.23",
            sha256="e7f24f87102d70268cff04bebf5a443bc3388f871aca53a01777d8938b8664c0",
            expand=False,
            url="https://files.pythonhosted.org/packages/6d/0f/6d2a97d10ebe0c67c5cc887d5abef3b62409adb1355ae872357baba41765/bpnet-0.0.23-py3-none-any.whl",
        )
        version(
            "0.0.22",
            sha256="fa69eaa4283b9f4fa5fe8a005fa2bd72e6588cdcb6c2fab553c1ead5732f022b",
            expand=False,
            url="https://files.pythonhosted.org/packages/40/d0/8c96ee34d8316ca850d0a6713a7e0bcf18efc827e1872735cb2c889393e3/bpnet-0.0.22-py3-none-any.whl",
        )

    version(
        "2.0.0",
        sha256="dccff1bfe7c1d726967e95e270b712a9eacd580756d80f6c19ae55ea1be43633",
        expand=False,
        url="https://files.pythonhosted.org/packages/23/50/4829059e3a47964ce969eabdac44ee0d2367b4381cf41cbf7782a2938e6d/bpnet-2.0.0-py3-none-any.whl",
    )

    depends_on("python@3.7:3.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")

    depends_on("py-tensorflow", when="@2.0.0", type=("build", "run"))
    depends_on("py-tensorflow-probability@0.12.1", when="@2.0.0", type=("build", "run"))
    depends_on("py-pysam", when="@2.0.0", type=("build", "run"))
    depends_on("py-py2bit", when="@2.0.0", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-deepdish", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-deeptools", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-deeplift", type=("build", "run"))

    def install_test(self):
        with working_dir("spack-test", create=True):
            which("bpnet-counts-loss-weight")("--help")
