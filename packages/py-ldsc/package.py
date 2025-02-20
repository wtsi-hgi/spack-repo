# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLdsc(PythonPackage):
    """LD Score Regression (LDSC)"""

    homepage = "http://github.com/bulik/ldsc"
    pypi = "ldsc/ldsc-2.0.1-py3-none-any.whl"

    version(
        "2.0.0",
        sha256="2ed8b9a6056547a57570c64aadd41eb4b117143740594cc7dd1a121dfa468f9c",
        expand=False,
        url="https://files.pythonhosted.org/packages/11/cd/b2a051b515b1783c6c1941dd5fbd164f3f2a39765afa966b597a16f0db96/ldsc-2.0.0-py3-none-any.whl",
    )
    version(
        "2.0.1",
        sha256="6780af857d866a7c3fc987aef346887a719ba8564cc33ec6e626ffc6940bac43",
        expand=False,
        url="https://files.pythonhosted.org/packages/e5/28/0039f95b8c7d9db1f5623eeb9ff3260bb436c9f63a99e7feb429dfefeaad/ldsc-2.0.1-py3-none-any.whl",
    )

    depends_on("python@:3.9", type=("build", "run"))
    depends_on("py-setuptools", type=("build"))
    depends_on("py-bitarray", type=("build", "run"))
    depends_on("py-nose", type=("build", "run"))
    depends_on("py-pybedtools@0.9.1:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))


# {'bitarray(==2.6.0)': ['2.0.0'], 'nose(==1.3.7)': ['2.0.0'], 'pybedtools(==0.9.0)': ['2.0.0'], 'scipy(==1.9.2)': ['2.0.0'], 'numpy(==1.23.3)': ['2.0.0'], 'pandas(==1.5.0)': ['2.0.0'], 'bitarray(>=2.6.0)': ['2.0.1'], 'nose(>=1.3.7)': ['2.0.1'], 'pybedtools(>=0.9.0)': ['2.0.1'], 'scipy(>=1.9.2)': ['2.0.1'], 'numpy(>=1.23.3)': ['2.0.1'], 'pandas(>=1.5.0)': ['2.0.1']}
