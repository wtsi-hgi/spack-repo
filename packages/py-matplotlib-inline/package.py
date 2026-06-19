# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMatplotlibInline(PythonPackage):
    """Inline Matplotlib backend for Jupyter."""

    homepage = "https://github.com/ipython/matplotlib-inline"
    pypi = "matplotlib-inline/matplotlib-inline-0.1.2.tar.gz"

    version("0.2.2", sha256="72f3fe8fce36b70d4a5b612f899090cd0401deddc4ea90e1572b9f4bfb058c79", url="https://files.pythonhosted.org/packages/bd/c0/9f7c9a46090390368a4d7bcb76bb87a4a36c421e4c0792cdb53486ffac7a/matplotlib_inline-0.2.2.tar.gz")
    version("0.1.7", sha256="8423b23ec666be3d16e16b60bdd8ac4e86e840ebd1dd11a30b9f117f2fa0ab90", url="https://files.pythonhosted.org/packages/99/5b/a36a337438a14116b16480db471ad061c36c3694df7c2084a0da7ba538b7/matplotlib_inline-0.1.7.tar.gz")
    version("0.1.6", sha256="f887e5f10ba98e8d2b150ddcf4702c1e5f8b3a20005eb0f74bfdbd360ee6f304")
    version("0.1.3", sha256="a04bfba22e0d1395479f866853ec1ee28eea1485c1d69a6faf00dc3e24ff34ee")
    version("0.1.2", sha256="f41d5ff73c9f5385775d5c0bc13b424535c8402fe70ea8210f93e11f3683993e")

    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-traitlets", type=("build", "run"))
    depends_on("py-flit-core@3.2:", type="build", when="@0.2.2:")
