# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyarrowHotfix(PythonPackage):
    """None"""
    
    homepage = "None"
    pypi = "pyarrow-hotfix/pyarrow_hotfix-0.7-py3-none-any.whl" 

    version("0.3", sha256="ba15b5ef8cae9d7baebd14dd86e87593cd3b137b54c05321cc8cc5c6e0523ff7", expand=False, url="https://files.pythonhosted.org/packages/ad/8a/09b15a86fcdfee5de96d0d203a035ec94d5f1b590b664362a746c8a0b8b6/pyarrow_hotfix-0.3-py3-none-any.whl")
    version("0.4", sha256="aecaecaccbe4b3d7b7198d6634afe1c5eec3cbf89d1b551e9f85675f21b24921", expand=False, url="https://files.pythonhosted.org/packages/7d/89/e54aa4edba6f30d8799d4d4f9075443be6fae839d57cf6ba464bb4a2d5ab/pyarrow_hotfix-0.4-py3-none-any.whl")
    version("0.5", sha256="7e20a1195f2e0dd7b50dffb9f90699481acfce3176bfbfb53eded04f34c4f7c6", expand=False, url="https://files.pythonhosted.org/packages/36/9d/fed46a4d94d05bc400bdaeb02d277ca5e61965cebe25b6029990d2191c0b/pyarrow_hotfix-0.5-py3-none-any.whl")
    version("0.6", sha256="dcc9ae2d220dff0083be6a9aa8e0cdee5182ad358d4931fce825c545e5c89178", expand=False, url="https://files.pythonhosted.org/packages/e4/f4/9ec2222f5f5f8ea04f66f184caafd991a39c8782e31f5b0266f101cb68ca/pyarrow_hotfix-0.6-py3-none-any.whl")
    version("0.7", sha256="3236f3b5f1260f0e2ac070a55c1a7b339c4bb7267839bd2015e283234e758100", expand=False, url="https://files.pythonhosted.org/packages/2e/c3/94ade4906a2f88bc935772f59c934013b4205e773bcb4239db114a6da136/pyarrow_hotfix-0.7-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.5:", type=("build", "run"))
