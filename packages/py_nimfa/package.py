# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNimfa(PythonPackage):
    """A Python module for nonnegative matrix factorization"""

    homepage = "http://nimfa.biolab.si"
    pypi = "nimfa/nimfa-1.4.0-py2.py3-none-any.whl"

    version("1.0", sha256="0c1104be00b96cfd181068c987e9ef1cf1689d75c179373fe3211b20e6256cf2")
    version("1.1", sha256="de403cb0dc50f00e0c81f44a14eb5ea3157b7b36456da884a24d24d07608fd69")
    version("1.2.2", sha256="6a4bf4e9df7df5c02a58bfb73dacb8bdbc1c7504d248f426ee96ec187fcd903d")
    version("1.2.3", sha256="7f6b93061f454974ee916a630d37574337195db3766f2283c351e6201430b37b")
    version("1.3.0", sha256="825ba13dc7d05363f567b8b2d492fa759f7208440a43f37200d1a22d3d03b5e1")
    version("1.3.1", sha256="451a6bd440fdecf685d16997f94e3a233944b282a19e4c92e4e62d936ca9a015")
    version("1.3.2", sha256="87171493f5af8201297ea67938342e98277e7726ae8ff010b4c7738948ce0c47")
    version("1.3.3", sha256="b925482f90fc68eae50b4b72e4272e9b89b86cf6edf6778aedd989130e33b349")
    version("1.3.4", sha256="651376eba6b049fe270dc0d29d4b2abecb5e998c2013df6735a97875503e2ffe")
    version(
        "1.4.0",
        sha256="d9f2e1419c94524cec79e8d19291180707a2052ac2e25284edaba235d1575451",
        expand=False,
        url="https://files.pythonhosted.org/packages/75/e3/1f5626e07fa38b9fd5bf92c018b97e8dd4eec69dd6284b1294fd46873e66/nimfa-1.4.0-py2.py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))


# {'numpy(>=1.7.0)': ['1.4.0'], 'scipy(>=0.12.0)': ['1.4.0']}
