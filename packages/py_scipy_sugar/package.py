# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScipySugar(PythonPackage):
    """Missing SciPy functionalities."""

    homepage = "https://github.com/limix/scipy-sugar"
    pypi = "scipy-sugar/scipy-sugar-1.0.9.tar.gz"

    version("1.0.9", sha256="d88d723afbcdcbec81996d2f8723b980d7a43fecf5da3d05ece5c10bfa32fcf1")
    version("1.0.8", sha256="39c419dc016414e540b971b3dde49f0f75260b7131a8917f2038b7c511715cef")
    version("1.0.7", sha256="4d03047641311b7b4cbe60f59a41f1fc46852b7ea0184c6fff204b7e5537fbb4")
    version("1.0.6", sha256="d06fd7a301dcb3e9d178f3d9bb6f796ce999781c2cc4f9e08fab2c65ef0e3abf")
    version("1.0.5", sha256="3d8f727e11d6be895c99acb4000f732fda562f4dc8fec3de1f5a4a48a0a53f26")
    version("1.0.4", sha256="12a4c04dc80823831363e88d11e4491e580b9ebbb55797683ee3c0c5b12c55c8")
    version("1.0.2", sha256="2942681512256c40bc7801a38701b12b5dff413dd6c4d04aafd1ee79d36529b1")
    version("1.0.1", sha256="6b7a2b52d8d3cec6e25444178f455b24793ed9cd65b05c8dca35b0c4e3d24a89")
    version("1.0.0", sha256="4857732f8578b462d3b636d4b6dc61fd7c9b7960401917ee2bb19c0e6fdfa022")

    depends_on("py-setuptools", type="build")
    depends_on("py-pytest-runner@4.2:", type="build")
    depends_on("py-numpy@1.14.3:", type=("build", "run"))
    depends_on("py-optimix@1.2.23:", type=("build", "run"))
    depends_on("py-pytest@3.6.2:", type=("build", "run"))
    depends_on("py-pytest-doctestplus@0.1.3:", type=("build", "run"))
    depends_on("py-scipy@1.0.1:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import scipy_sugar")
