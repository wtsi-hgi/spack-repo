# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDenovowest(PythonPackage):
    """A de novo mutation simulation framework"""
    
    homepage = "None"
    pypi = "denovowest/denovowest-0.1.2-py3-none-any.whl" 

    version("0.1.1", sha256="ecbb999734c0e9fc4b53e7007418d0bbcb3b1fcebb6ce6975ab7b66a4d6b8f83", expand=False, url="https://files.pythonhosted.org/packages/f3/8e/39d227ea33a475913bf3729b4ad78ecce644d50a7a5cc2f1bbbbc8e2cbb3/denovowest-0.1.1-py3-none-any.whl")
    version("0.1.2", sha256="8f28112ac778428542bf838b1e23a1234fdf164d34e5be1b0d9c0bb421fa39a2", expand=False, url="https://files.pythonhosted.org/packages/91/74/9a49b8ea832e5e9d3b7a9a27a518eeff683f00cba501eb55ef2ba19a6275/denovowest-0.1.2-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-gffutils", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))

# {'numpy': ['0.1.1', '0.1.2'], 'scipy': ['0.1.1', '0.1.2'], 'pandas': ['0.1.1', '0.1.2'], 'gffutils': ['0.1.1', '0.1.2'], 'click': ['0.1.1', '0.1.2'], 'pyyaml': ['0.1.1', '0.1.2'], 'pysam': ['0.1.1', '0.1.2'], 'joblib': ['0.1.1', '0.1.2']}