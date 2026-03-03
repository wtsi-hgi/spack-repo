# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPytoda(PythonPackage):
    """pytoda: PaccMann PyTorch Dataset Classes."""

    homepage = "https://github.com/PaccMann/paccmann_datasets"
    pypi = "pytoda/pytoda-1.1.5-py3-none-any.whl"

    version(
        "1.0.0",
        sha256="f4261f30119c2680e9eb0fe3af8817e003c063aa8306053cbf85ad0c7ab8525e",
        expand=False,
        url="https://files.pythonhosted.org/packages/e9/05/1224ed38123ce71073df0beee29c3d93b090d7ef87102116f4a6b25d03ad/pytoda-1.0.0-py3-none-any.whl",
    )
    version(
        "1.0.1",
        sha256="869daa152472f4bbee6f4310bf05fc43fc96174f0ef910549bcd3667d0bf6e7d",
        expand=False,
        url="https://files.pythonhosted.org/packages/2a/e4/101d62deffbde99b842fe7e3f4f5236ef94b48c26fc6ab450ba258f9aae3/pytoda-1.0.1-py3-none-any.whl",
    )
    version(
        "1.0.2",
        sha256="5eba04035f6b48d2b6edc27f4057d28e40ed8654b71728392dd0f77b34a14770",
        expand=False,
        url="https://files.pythonhosted.org/packages/6e/1a/bf7e804bcb0f22cc1d054b1365a72bfb492e2b2baa7f6765b9ea9c59bcf0/pytoda-1.0.2-py3-none-any.whl",
    )
    version(
        "1.1.0",
        sha256="ee488ecf32a132270a66825b5663895e3f025f905f051b4f390a45fead40e704",
        expand=False,
        url="https://files.pythonhosted.org/packages/59/65/794e9146237ebdc21920b6b5ecb4653914a3944e5c752c948158433adc05/pytoda-1.1.0-py3-none-any.whl",
    )
    version(
        "1.1.1",
        sha256="2cda8a92361f781c63786825930d094052516aca8ae59ab98c794804baba3212",
        expand=False,
        url="https://files.pythonhosted.org/packages/41/77/ad617548c1ab44afa663570426b1836c87d72e59d5134d226c2626ba2818/pytoda-1.1.1-py3-none-any.whl",
    )
    version(
        "1.1.2",
        sha256="a62d597a3ec67f266d5b6167565afb964b537b4838c9eed015a5c71be1ea5b3a",
        expand=False,
        url="https://files.pythonhosted.org/packages/44/b3/25f83d38d5f81f62efe4463acf22ea72373e07aeb7e37663cf7c11824f79/pytoda-1.1.2-py3-none-any.whl",
    )
    version(
        "1.1.3",
        sha256="38692b00a5d51a24996dfd08128c1ac36aebffa8672c94cdb1bb05376f3eef0f",
        expand=False,
        url="https://files.pythonhosted.org/packages/ca/66/8445f76dd0be3680c643577b2217658583c97c4736d830ab4b33426b6c0a/pytoda-1.1.3-py3-none-any.whl",
    )
    version(
        "1.1.4",
        sha256="44c1022ac5be1fc04a3d5746836100fca50588f47207472df1e5dd1718a6785d",
        expand=False,
        url="https://files.pythonhosted.org/packages/12/54/b62bc44e005aae072f7c5188631e8684750ba39af0756e06e7a580c6e399/pytoda-1.1.4-py3-none-any.whl",
    )
    version(
        "1.1.5",
        sha256="b8f29ad4b936e13229ca148dc7331219f5aaf690d14ecbd6a87cf6fb893ca4f0",
        expand=False,
        url="https://files.pythonhosted.org/packages/16/d7/a0049153273201cb5a5ac285cae1ee7ce6da5ba81c639e94bd3bd76f56e6/pytoda-1.1.5-py3-none-any.whl",
    )

    depends_on("python@3.11:", type=("build", "run"))
    depends_on("rdkit", type=("build", "run"))
    depends_on("py-unidecode", type=("build", "run"))
    depends_on("py-importlib-resources", type=("build", "run"))
    depends_on("py-pubchempy", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-smilespe", type=("build", "run"))
    depends_on("py-upfp", type=("build", "run"))
    depends_on("py-selfies", type=("build", "run"))
    depends_on("py-dill", type=("build", "run"))
    depends_on("py-diskcache", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))


# {'numpy': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'scikit-learn': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'pandas': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'torch(>=1.0.0)': ['1.0.0'], 'diskcache': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'dill': ['1.0.0'], 'selfies(>=2.0.0)': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1'], 'upfp': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'SmilesPE(>=0.0.3)': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'pyfaidx': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'pubchempy': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'importlib-resources': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'Unidecode': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'rdkit-pypi(>=2021.9.3)': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'torch(>=1.4.0)': ['1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'dill(>=0.3.3)': ['1.0.1', '1.0.2', '1.1.0', '1.1.1', '1.1.2', '1.1.3'], 'selfies(>=2.1.1)': ['1.1.2', '1.1.3'], 'torch>=1.4.0': ['1.1.4', '1.1.5'], 'dill>=0.3.3': ['1.1.4', '1.1.5'], 'selfies>=2.1.1': ['1.1.4', '1.1.5'], 'SmilesPE>=0.0.3': ['1.1.4', '1.1.5'], 'rdkit-pypi>=2021.9.3': ['1.1.4'], 'rdkit': ['1.1.5']}
