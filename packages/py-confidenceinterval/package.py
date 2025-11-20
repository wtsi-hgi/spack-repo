# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyConfidenceinterval(PythonPackage):
    """Confidence intervals utilities for Python."""

    homepage = "https://github.com/jacobgil/confidenceinterval"
    pypi = "confidenceinterval/confidenceinterval-1.0.5.tar.gz"

    version("1.0.5", sha256="38552f7124cff7058845b97e19e0790411cf5bf842a142012056fdeb3749728d")
    version("1.0.4", sha256="159af90d9135f67f6140a40728a7d87ade875d0aec9d52da6b0f565d81a51523")
    version("1.0.3", sha256="a1e58ed34ba63daf4a9a3b11351a5bfc941abadad32310b73082997d6af7d683")
    version("1.0.2", sha256="80ee922792a4760aaeb0d864fe33acde99ad096c6a53a0e3af875e45a2dcc373")
    version("1.0.1", sha256="28481668d71b4035725b1559c656c183138db8dcc6e5f658f5322d0bb9f3f8aa")
    version("1.0.0", sha256="a3df29ebabe449bff85f177bf2270caee7990e1e5b80d55ac52ee2eb7c5b0008")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import confidenceinterval")
