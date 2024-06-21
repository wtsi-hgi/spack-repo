# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCrispat(PythonPackage):
    """CRISPR guide assignment tool"""

    homepage = "https://github.com/velten-group/crispat/tree/main"
    pypi = "crispat/crispat-0.9.3-py3-none-any.whl"

    version(
        "0.9.1",
        sha256="7e2c99483bb015a4a2237bfd2390e8fc0730f8065d8660b6f11ef5ed7248b3b8",
        expand=False,
        url="https://files.pythonhosted.org/packages/cf/27/dc8b301e3ec8d13850e3575055f7294032c6e18e593c20607f2e2177d944/crispat-0.9.1-py3-none-any.whl",
    )
    version(
        "0.9.3",
        sha256="38a669bf670271e077e7f51ec0e396cc41e6da1c7a40917641d64ee19fe66a46",
        expand=False,
        url="https://files.pythonhosted.org/packages/36/f0/59605763057a49561a6a10f76e414a88476cd9e7cfbfe71757a66bd00fc8/crispat-0.9.3-py3-none-any.whl",
    )

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-pyro-ppl", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))


# {'anndata>=0.8.0': ['0.9.1', '0.9.3'], 'matplotlib>=3.7.1': ['0.9.1', '0.9.3'], 'numpy==1.24.3': ['0.9.1', '0.9.3'], 'pandas>=1.5.3': ['0.9.1', '0.9.3'], 'pyro-ppl>=1.8.6': ['0.9.1', '0.9.3'], 'scanpy>=1.9.3': ['0.9.1', '0.9.3'], 'scipy>=1.9.3': ['0.9.1', '0.9.3'], 'seaborn>=0.12.2': ['0.9.1', '0.9.3'], 'setuptools>=69.5.1': ['0.9.1', '0.9.3'], 'torch>=2.0.1': ['0.9.1', '0.9.3'], 'tqdm>=4.65.0': ['0.9.1'], 'tqdm>=4.66.3': ['0.9.3']}
