# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFastHistogram(PythonPackage):
    """Fast simple 1D and 2D histograms"""

    homepage = "https://github.com/astrofrog/fast-histogram"
    pypi = "fast-histogram/fast_histogram-0.14.tar.gz"

    version("0.1", sha256="a3d5404d420530ce62368c4383697febde36ad0ea586fdd8b0e6c3699aed323e")
    version("0.10", sha256="6404fff03464aff630d5e3183d8e3c258788ac5f38f615a45b981077fe050e78")
    version("0.11", sha256="9acb6fa5b6efd928663008965da186962bdeae20e6d5bbb3b1195dfbd1d906f0")
    version("0.13", sha256="da27a74b5ad7ebaf04b4a855c2ade39a9d41fbdb6ee7f07cba159422045c7af2")
    version("0.14", sha256="390973b98af22bda85c29dcf6f008ba0d626321e9bd3f5a9d7a43e5690ea69ea")
    version("0.2", sha256="e3f563db22478a950a24a52b11786114a8ad90c72addd7bd72e7e5a7d2159ece")
    version("0.2.1", sha256="1cbefcb23a8fad6f904b73a6a8d7cc04127e3691cbb6f0cdd4fdd20a94f0dd0c")
    version("0.3", sha256="fdfab401aed9ba2bf96cac2f41679dbb26e0da520e7fd0428e8b1aa20b47ac0d")
    version("0.4", sha256="8afcea57930c9ede74ce304a45c5374128485e83c4c9ad143a8778c5ed281419")
    version("0.5", sha256="0e3849e244909aa68e58305ed101c19c8576176eaf90fd5d79215d5ade51a6a7")
    version("0.6", sha256="eb532a21fd58aec20c083a2c900527a4f9e9894fe64ed2f57a538871c9343d13")
    version(
        "0.7",
        sha256="9890fdcef36ca7d16ab36b780d3cc7e6dad2b1c9bb961eb6f7e2e677b44f5dd9",
        expand=False,
        url="https://files.pythonhosted.org/packages/cf/1c/42ac0b4355c2d3383e8286d3501cc4aaab0ccbed2c7abbdcb7997382d145/fast_histogram-0.7-cp37-cp37m-manylinux1_x86_64.whl",
    )
    version(
        "0.8",
        sha256="ace39b2a388f6a44de78f917a86a7436076ac12e9da76a3ea7a7a513c474abc5",
        expand=False,
        url="https://files.pythonhosted.org/packages/ca/55/5df54bcc19472ad880a79d75d9681ea0f9e4147111e8d4babe8a57badf11/fast_histogram-0.8-cp38-cp38-manylinux1_x86_64.whl",
    )
    version(
        "0.9",
        sha256="68a22443a9f1436cae157e653db05ac91c27d7f297e5260c7c2d111e9c93e783",
        expand=False,
        url="https://files.pythonhosted.org/packages/69/73/33e99d223f1339e87d32c3fd4cd837150a79283e1154c04dd359aa397a5b/fast_histogram-0.9-cp38-cp38-manylinux1_x86_64.whl",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
