# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDeepdish(PythonPackage):
    """Deep Learning experiments from University of Chicago."""

    homepage = "https://github.com/uchicago-cs/deepdish"
    pypi = "deepdish/deepdish-0.3.7-py2.py3-none-any.whl"

    version("0.1.1", sha256="feb0a9f5b865722d1a89c145fb5d267a35c6978e2e09bf34835b98b65414ec76")
    version("0.1.2", sha256="50192107d660bd25df44071bf45278aaeefa7a859f173858fa228aa8b0571b02")
    version("0.1.3", sha256="360d8f1975c379bf16c5b6616f44cfbc8d7b581e945c04e5f7fb6efc049660de")
    version("0.1.4", sha256="2960952b2282057730004b5894e2a0f720fc1d0e2243e7fb28ae0bc98ca705b9")
    version("0.1.5", sha256="20332482d3081bcb7a5dd6c8072aae66bd3d58ce734dc8ea0fc44a389071ee8b")
    version("0.1.6", sha256="d5820fc434d5c39c00d50263bccc60f7db83f688b3de6e238c06c4817fba3470")
    version("0.1.7", sha256="5781b45677b053affc7e64b171ab6c2b6ee7b4361c8d2a776bb47c44b085f79b")
    version("0.1.8", sha256="c94a21fff9a6c6d5f72dad8baa85f46ba865f9a70efcb06c70410e1c38e598e8")
    version("0.2.0", sha256="8610d68f4dc34f001b67d5fed4c1eb0bcbc5930c45cd3a33bfd9bb5bddbfe6be")
    version("0.3.4", sha256="7bf4cdd07bde69af93cd21b1e94e1da5dffddb4601db0eb78c5fa0dbde74d909", expand=False, url="https://files.pythonhosted.org/packages/23/0f/6f28946d23bc1bb6a2138d7118d6e6375b20718ec2807977d36bb70f313f/deepdish-0.3.4-py2.py3-none-any.whl")
    version("0.3.5", sha256="95ab7f064502ca9ee0391988b7157ed622b4da4f9f88de223c3dc382240c3b3a", expand=False, url="https://files.pythonhosted.org/packages/db/58/fdeab36c6024a8617d5585fca63c9f8256414dc5c9143133dfe3820a9a71/deepdish-0.3.5-py2.py3-none-any.whl")
    version("0.3.6", sha256="2b1d3d2a32356909f2618c382a1829347990ad81b63aaecc87b35a046cd3034c", expand=False, url="https://files.pythonhosted.org/packages/6e/39/2a47c852651982bc5eb39212ac110284dd20126bdc7b49bde401a0139f5d/deepdish-0.3.6-py2.py3-none-any.whl")
    version("0.3.7", sha256="272d6b075239efe66dd3e6d4e89bb6b0ffe68b0d9ce4f823e4e1c4549c4a294a", expand=False, url="https://files.pythonhosted.org/packages/d5/9b/7a0e11d7858feac24372ae770575802833436a050f93dfd012d8025e4ae9/deepdish-0.3.7-py2.py3-none-any.whl")

    depends_on("python")
    depends_on("py-setuptools", type=("build"))

    with default_args(type=("build", "run")):
        depends_on("py-tables", when="@0.3.2:")
        depends_on("py-scipy", when="@0.1.7:")
        depends_on("py-numpy", when="@.1.1:")

        depends_on("py-scikit-image", when="@0.1.4:0.3.0")
        depends_on("py-matplotlib", when="@0.1.4:0.3.0")
        
        depends_on("py-cython", when="@0.1.1:0.3.0")

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        python("-c", "import deepdish")
