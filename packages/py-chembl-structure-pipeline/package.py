# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyChemblStructurePipeline(PythonPackage):
    """ChEMBL Structure Pipeline"""
    
    homepage = "https://www.ebi.ac.uk/chembl/"
    pypi = "chembl-structure-pipeline/chembl_structure_pipeline-1.2.2-py3-none-any.whl" 

    version("1.1.0", sha256="ee801ab0f908216ad0da0256ef6b14ee5d4428378a0bb89d0f551a2482f91f9a", expand=False, url="https://files.pythonhosted.org/packages/2c/9a/fb66f05852d8daa3ffd35c4d484a16a25a42c1d6a311cbc2d5def8371b42/chembl_structure_pipeline-1.1.0-py3-none-any.whl")
    version("1.2.0", sha256="e45d7775073025d91def90e0b8a11ea7793e550ba10956cda3a253f4202683f7", expand=False, url="https://files.pythonhosted.org/packages/db/54/44dff855e912c13a8974c73f7ecc0bb5239c34d02fc7563078e8392f13e6/chembl_structure_pipeline-1.2.0-py3-none-any.whl")
    version("1.2.2", sha256="fe7fdcc87e276223af721b0111503c4f168b36fae92257420c00f73515c6485d", expand=False, url="https://files.pythonhosted.org/packages/97/57/6813202cfe8afe187ac01c3e96396fca5727309de016309b3d1fda351b84/chembl_structure_pipeline-1.2.2-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-rdkit", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))

# {'setuptools(>=46.4.0)': ['1.1.0', '1.2.0'], 'rdkit(>=2022.09.01)': ['1.1.0', '1.2.0'], 'setuptools>=46.4.0': ['1.2.2'], 'rdkit>=2022.09.01': ['1.2.2']}